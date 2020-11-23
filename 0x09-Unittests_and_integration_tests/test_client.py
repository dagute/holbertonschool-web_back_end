#!/usr/bin/env python3
"""TestClient module"""

import unittest
from unittest import mock
from unittest.mock import PropertyMock, Mock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Testing GithubOrgClient class"""
    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc", {"payload": True}),
    ])
    @patch("client.get_json")
    def test_org(self, x, y, mock_get):
        """test_org"""
        mock_get.return_value = y
        git_c = GithubOrgClient(x)
        res = git_c.org
        self.assertEqual(res, y)
        mock_get.assert_called_once()

    def test_public_repos_url(self):
        """test_public_repos_url"""
        with mock.patch.object(GithubOrgClient,
                               "org",
                               new_callable=PropertyMock) as mock_g:
            json_t = {"url": "google", "repos_url": "http://google.com"}
            mock_g.return_value = json_t
            git_c = GithubOrgClient(json_t.get("google"))
            res = git_c._public_repos_url
            mock_g.assert_called_once()
            self.assertEqual(res, test_json.get("repos_url"))

    @patch('client.get_json')
    def test_public_repos(self, m_get_json):
        """test_public_repos"""
        m_get_json.return_value = [{"name": "google"},
                                   {"name": "abc"}]
        with mock.patch.object(GithubOrgClient, "_public_repos_url",
                               new_callable=PropertyMock) as mock_g:
            mock_g.return_value = "http://google.com"
            g = GithubOrgClient("facebook")
            res = g.public_repos()
            self.assertEqual(res, ["google", "abc"])
            m_get_json.assert_called_once()
            mock_g.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)])
    def test_has_license(self, x, y, z):
        """
        test_has_license.
        """
        git_c = GithubOrgClient("google")
        res = git_c.has_license(x, y)
        self.assertEqual(res, z)
