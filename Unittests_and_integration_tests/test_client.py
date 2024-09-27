#!/usr/bin/env python3
"""
Parameterize and patch as decorators
"""
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized
from utils import get_json
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value
        """
        mock_json_call.return_value = {"data": True}
        self.assertEqual(github_client.org, {"data": True})
        mock_json_call.assert_called_once()

    def test_public_repos_url(self):
        """
        Mocking a property
        """
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "http://cats.com"}
            github_client = GithubOrgClient("test")
            self.assertEqual(github_client._public_repos_url,
                             "http://cats.com")

    @patch("client.get_json")
    @patch.object(GithubOrgClient, "_public_repos_url",
                  new_callable=PropertyMock)
    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        Payload return for repo
        """
        mock_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]

        mock_get_json.return_value = mock_payload
        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=property
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = (
                "https://api.github.com/orgs/test-org/repos"
            )

            github_client = GithubOrgClient("test-org")
            repos = github_client.public_repos()
            self.assertEqual(repos, ["repo1", "repo2", "repo3"])
            mock_public_repos_url.assert_called_once()

            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/test-org/repos"
            )

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_value):
        """
        Test that has_license returns the correct value
        """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected_value)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up
        """
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            if url == "https://api.github.com/orgs/google":
                return patch('requests.Response',
                             json=lambda: cls.org_payload)
            elif url == "https://api.github.com/orgs/google/repos":
                return patch('requests.Response',
                             json=lambda: cls.repos_payload)
            return None

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """
        Stop the patcher after tests
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Test public_repos returns the expected list of repositories
        """
        github_client = GithubOrgClient("google")
        repos = github_client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """
        Test public_repos with a specific license
        """
        github_client = GithubOrgClient("google")
        repos = github_client.public_repos(license="apache-2.0")
        self.assertEqual(repos, self.apache2_repos)
