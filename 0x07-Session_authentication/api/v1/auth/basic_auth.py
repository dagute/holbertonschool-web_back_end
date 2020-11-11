#!/usr/bin/env python3
"""
Basic auth
"""

from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """BasicAuth class"""

    def extract_base64_authorization_header(self, au_h: str) -> str:
        """
        extract_base64_authorization_header
        """
        if not au_h or type(au_h) != str or not au_h.startswith("Basic "):
            return
        return au_h[6:]

    def decode_base64_authorization_header(self, b64_au_h: str) -> str:
        """
        decode_base64_authorization_header
        """
        if not b64_au_h or not isinstance(b64_au_h, str):
            return None
        try:
            b = base64.b64decode(b64_au_h)
            decoded = b.decode("utf-8")
        except Exception:
            return None
        return decoded

    def extract_user_credentials(self, db64: str) -> (str, str):
        """
        extract_user_credentials
        """
        if not db64 or type(db64) != str or ":" not in db64:
            return (None, None)
        credentials = db64.split(":", 1)
        return (credentials[0], credentials[1])

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """
        user_object_from_credentials
        """
        if not user_email or not user_pwd or \
           not isinstance(user_email, str) or not isinstance(user_pwd, str):
            return None
        try:
            user = User.search({'email': user_email})
        except Exception:
            return None
        if user:
            for u in user:
                if u.is_valid_password(user_pwd):
                    return u
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        current_user
        """
        try:
            header = self.authorization_header(request)
            b64_h = self.extract_base64_authorization_header(header)
            decoded = self.decode_base64_authorization_header(b64_h)
            cred = self.extract_user_credentials(decoded)
            return self.user_object_from_credentials(cred[0], cred[1])
        except Exception:
            return None
