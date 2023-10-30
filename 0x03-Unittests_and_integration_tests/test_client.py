#!/usr/bin/env python3
"""Unittest Module"""


from unittest import TestCase
from parameterized import parameterized
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient


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
