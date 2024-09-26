#!/usr/bin/env python 3
"""
Parameterize and patch as decorators
"""
import unittest
from unittest.mock import patch, Mock
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
