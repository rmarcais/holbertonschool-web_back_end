#!/usr/bin/env python3
"""test_utils module"""

from parameterized import parameterized
from typing import Any, Dict, Mapping, Sequence
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: Any) -> None:
        """Tests the access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'")
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence,
                                         expected: Any) -> None:
        """Tests the access_nested_map function"""
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(expected, str(error.exception))


class TestGetJson(unittest.TestCase):
    """TestGetJson class"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        """Tests the get_json function"""
        patcher = patch("requests.get")
        mock_get = patcher.start()

        mock_response = Mock()
        mock_response.json.return_value = test_payload

        mock_get.return_value = mock_response

        self.assertIsInstance(mock_get.return_value, Mock)
        self.assertEqual(get_json(test_url), test_payload)

        patcher.stop()


class TestMemoize(unittest.TestCase):
    """TestMemoize class"""

    def test_memoize(self) -> None:
        """Tests the memoize function"""

        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        my_obj = TestClass()
        with patch.object(my_obj, 'a_method') as mock_a_method:
            mock_a_method.return_value = 42
            result = my_obj.a_property
            self.assertEqual(result, 42)
            result = my_obj.a_property
            mock_a_method.assert_called_once()
