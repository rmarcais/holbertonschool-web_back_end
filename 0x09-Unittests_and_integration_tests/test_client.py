#!/usr/bin/env python3
"""test_client module"""

from parameterized import parameterized
from typing import Any, Dict, Mapping, Sequence
from client import GithubOrgClient
from unittest.mock import patch, Mock
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class"""

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, org: str, mock_get_json) -> None:
        """Tests the org method"""
        mock_get_json.return_value = {}

        client = GithubOrgClient(org)
        result = client.org
        result = client.org
        self.assertEqual(result, {})
        mock_get_json.assert_called_once()
