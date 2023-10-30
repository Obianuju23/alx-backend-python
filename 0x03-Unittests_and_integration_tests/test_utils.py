#!/usr/bin/env python3
"""Unittest Module"""
from unittest import TestCase
from parameterized import parameterized
from utils import access_nested_map
from unittest.mock import patch, Mock
from utils import get_json


class TestAccessNestedMap(TestCase):
    """Class that test Nested map function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected_result):
        """Test that the method returns the expected outcome"""
        real_result = access_nested_map(map, path)
        self.assertEqual(real_result, expected_result)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, map, path, wrong_result):
        """Method that tests&handles errors from access_nested_map function"""
        with self.assertRaises(KeyError) as err:
            access_nested_map(map, path)
            self.assertEqual(wrong_result, str(err.exception))


class TestGetJson(TestCase):
    """Class that tests get_json function"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """method to test that utils.get_json returns the expected result"""
        mock_response = Mock()
        # This sets mock respond to have return value of test payload
        mock_response.json.return_value = test_payload
        # function that calls request.get&needs patch to get mock return value
        with patch('requests.get', return_value=mock_response):
            real_response = get_json(test_url)
            self.assertEqual(real_response, test_payload)
            # ensures that mock method is calleed only once
            mock_response.json.assert_called_once()


class TestMemoize(TestCase):
    """A class that test for memoization"""
    def test_memoize(self):
        """ This is memoize function tests """

        class TestClass:
            """ A Test class """

            def a_method(self):
                """ Method to always return 42 """
                return 42

            @memoize
            def a_property(self):
                """ Returns memoized property """
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as patched:
            test_class = TestClass()
            real_return = test_class.a_property
            real_return = test_class.a_property

            self.assertEqual(real_return, 42)
            patched.assert_called_once()