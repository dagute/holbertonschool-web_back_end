#!/usr/bin/env python3
""" python unittest """
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import patch, Mock
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class"""

    @parameterized.expand([({"a": 1}, ("a",), 1),
                           ({"a": {"b": 2}}, ("a",), {"b": 2}),
                           ({"a": {"b": 2}}, ("a", "b"), 2)])
    def test_access_nested_map(self, x, y, z):
        """test_access_nested_map"""
        return self.assertEqual(access_nested_map(x, y), z)

    @parameterized.expand([({}, ("a",)),
                           ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self, x, y):
        """
        test_access_nested_map_exception.
        """
        with self.assertRaises(KeyError):
            access_nested_map(x, y)


class TestGetJson(unittest.TestCase):
    """TestGetJson class"""

    @parameterized.expand([("http://example.com", {"payload": True}),
                           ("http://holberton.io", {"payload": False})])
    def test_get_json(self, x, y):
        """test_get_json"""

        class MyMock(Mock):
            """MyMock class"""

            def json(self):
                """json"""
                return y
        with patch('utils.requests.get') as mock_get:
            mock_get.return_value = MyMock()
            response = get_json(x)
            mock_get.assert_called_once_with(x)
            self.assertEqual(response, y)


class TestMemoize(unittest.TestCase):
    """TestMemoize Class"""
    def test_memoize(self):
        """Test memoize"""
        class TestClass:
            """A class for testing"""
            def a_method(self):
                """a_method"""
                return 42

            @memoize
            def a_property(self):
                """a_property"""
                return self.a_method()
        with patch.object(TestClass, "a_method") as mock_t:
            mock_t.return_value = True
            t = TestClass()
            t.a_property
            t.a_property
            mock_t.assert_called_once()


if __name__ == '__main__':
    unittest.main()
