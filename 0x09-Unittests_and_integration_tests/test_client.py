#!/usr/bin/env python3
"""test_client module"""

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
from typing import Dict
from unittest.mock import patch, PropertyMock, Mock
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


@parameterized_class([
    {"org_payload": TEST_PAYLOAD[0][0],
     "repos_payload": TEST_PAYLOAD[0][1],
     "expected_repos": TEST_PAYLOAD[0][2],
     "apache2_repos": TEST_PAYLOAD[0][3]}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """TestIntegrationGithubOrgClient class"""

    @classmethod
    def setUpClass(cls):
        """
        A class method called before tests
        in an individual class are run.
        """
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()
        mock_response_org = Mock()
        mock_response_org.json.return_value = cls.org_payload

        mock_response_repos = Mock()
        mock_response_repos.json.return_value = cls.repos_payload

        cls.mock_get.side_effect = [
            mock_response_org,
            mock_response_repos,
            mock_response_org,
            mock_response_repos
        ]

    @classmethod
    def tearDownClass(cls):
        """
        A class method called after tests
        in an individual class have run
        """
        cls.get_patcher.stop()

    def test_public_repos(self) -> None:
        """Tests the public_repos method"""
        client = GithubOrgClient("google")
        result = client.public_repos()
        self.assertEqual(result, self.expected_repos)

    def test_public_repos_with_license(self) -> None:
        """Tests the public_repos method with a license"""
        client = GithubOrgClient("google")
        result = client.public_repos("apache-2.0")
        self.assertEqual(result, self.apache2_repos)
