#!/usr/bin/env python3
""" Auth module containing the Auth class """

from flask import request
from typing import List, TypeVar


class Auth():
    """ Auth class """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Return False """
        if not path or not excluded_paths or excluded_paths == []:
            return True
        if path[-1] == "/":
            path = path[:-1]
        for i in range(len(excluded_paths)):
            if excluded_paths[i][-1] == "/":
                excluded_paths[i] = excluded_paths[i][:-1]
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Return None """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Retutn None """
        return None
