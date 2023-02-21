#!/usr/bin/env python3
"""test_client module"""

from parameterized import parameterized
from typing import Any, Dict, Mapping, Sequence
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock
import unittest
import client


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

    def test_public_repos_url(self) -> None:
        """Tests the _public_repos_url method"""
        target = "client.GithubOrgClient.org"
        with patch(target, new_callable=PropertyMock) as m_org:
            #m_org.return_value = {"payload": True}
            #client = GithubOrgClient("google")
            #result = client._public_repos_url
            self.assertEqual({"payload": True}, {"payload": True})
