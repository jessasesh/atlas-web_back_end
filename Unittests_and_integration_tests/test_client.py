#!/usr/bin/env python3
"""
Parameterize and patch as decorators
"""
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized
from utils import get_json


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


class TestGithubOrgClient(unittest.TestCase):

    def test_public_repos_url(self):
        """
        Moking a property
        """
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "http://cats.com"}
            github_client = GithubOrgClient("test")
            self.assertEqual(github_client._public_repos_url, "http://cats.com")

    @patch("client.get_json")
    @patch.object(GithubOrgClient, "_public_repos_url",
                  new_callable=PropertyMock)
