#!/usr/bin/env python3
"""test_client module"""

from parameterized import parameterized
from typing import Any, Dict, Mapping, Sequence
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock
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

    def test_public_repos_url(self) -> None:
        """Tests the _public_repos_url method"""
        target = "client.GithubOrgClient.org"
        with patch(target, new_callable=PropertyMock) as m_org:
            m_org.return_value = {"repos_url": "example"}
            client = GithubOrgClient("google")
            result = client.org
            self.assertEqual(result, {"repos_url": "example"})

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json) -> None:
        """Tests the public_repos method"""
        mock_get_json.return_value = [{"name": "hello"}, {"name": "world"}]

        target = "client.GithubOrgClient._public_repos_url"
        with patch(target, new_callable=PropertyMock) as m_public_repos_url:
            m_public_repos_url.return_value = "example"
            client = GithubOrgClient("google")
            result = client.public_repos()
            result = client.public_repos()
            self.assertEqual(result, ["hello", "world"])
            mock_get_json.assert_called_once()
            m_public_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo: Dict[str, Dict],
                         license_key: str, expected: bool) -> None:
        """Tests the has_license method"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)
