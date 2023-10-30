#!/usr/bin/env python3
"""Unittest Module"""
from unittest import TestCase
from parameterized import parameterized
from utils import access_nested_map


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
        """Method that tests and handles errors from access_nested_map function"""
        with self.assertRaises(KeyError) as err:
            access_nested_map(map, path)
            self.assertEqual(wrong_result, str(err.exception))
