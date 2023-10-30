#!/usr/bin/env python3
"""Unittest Module"""


from unittest import TestCase
from parameterized import parameterized
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized


class TestGithubOrgClient(TestCase):
    """A class that defines attributes used in testing testgithuborgclient"""

    @parameterized.expand([
        ("google", {"google": True}),
        ("abc", {"abc": True})
    ])
    @patch('client.get_json')
    def test_org(self, org, expected, get_patch):
        """Test the org of the client"""
        get_patch.return_value = expected
        spec = GithubOrgClient(org)
        self.assertEqual(spec.org, expected)
        get_patch.assert_called_once_with("https://api.github.com/orgs/"+org)

    def test_public_repos_url(self):
        """A method that test if test public response works"""
        expected = "www.yes.com"
        payload = {"repos_url": expected}
        to_mock = 'client.GithubOrgClient.org'
        with patch(to_mock, PropertyMock(return_value=payload)):
            cli = GithubOrgClient("spec")
            self.assertEqual(cli._public_repos_url, expected)

    @patch('client.get_json')
    def test_public_repos(self, get_json_mock):
        """ test the public repos function in client """
        Chris = {"name": "Chris", "license": {"key": "a"}}
        Uju = {"name": "Uju", "license": {"key": "b"}}
        Cheta = {"name": "Cheta"}
        to_mock = 'client.GithubOrgClient._public_repos_url'
        get_json_mock.return_value = [Chris, Uju, Cheta]
        with patch(to_mock, PropertyMock(return_value="www.yes.com")) as y:
            spec = GithubOrgClient("spec")
            self.assertEqual(spec.public_repos(), ['Chris', 'Uju', 'Cheta'])
            self.assertEqual(spec.public_repos("a"), ['Chris'])
            self.assertEqual(spec.public_repos("c"), [])
            self.assertEqual(spec.public_repos(45), [])
            get_json_mock.assert_called_once_with("www.yes.com")
            y.assert_called_once_with()

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, 'my_license', True),
        ({'license': {'key': 'other_license'}}, 'my_license', False)
    ])
    def test_has_license(self, repo, license, expected):
        """ test the license checker """
        self.assertEqual(GithubOrgClient.has_license(repo, license), expected)
    # @parameterized_class(
    #  ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    #  TEST_PAYLOAD
    # )
