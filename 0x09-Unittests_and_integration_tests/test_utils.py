#!/usr/bin/env python3
"""test_utils module"""

from parameterized import parameterized
from utils import access_nested_map
from utils import get_json
from unittest.mock import patch, Mock
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Tests the access_nested_map method"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'")
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Tests the access_nested_map method"""
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(expected, str(error.exception))


class TestGetJson(unittest.TestCase):
    """TestGetJson class"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Tests the get_json method"""
        patcher = patch("requests.get")
        mock_get = patcher.start()

        mock_response = Mock()
        mock_response.json.return_value = test_payload

        mock_get.return_value = mock_response

        self.assertIsInstance(mock_get.return_value, Mock)
        self.assertEqual(get_json(test_url), test_payload)

        patcher.stop()
