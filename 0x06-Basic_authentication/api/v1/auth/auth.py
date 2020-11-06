#!/usr/bin/env python3
"""Auth class
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """
    Auth class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        require_auth
        """
        if not path or not excluded_paths:
            return True
        if path[-1] != '/':
            path = path + '/'
        if path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        authorization_header
        """
        if request:
            return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """
        curent_user
        """
        return None
