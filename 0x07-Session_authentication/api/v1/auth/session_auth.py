#!/usr/bin/env python3
""" session_auth module containing the SessionAuth class """

from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


class SessionAuth(Auth):
    """ SessionAuth class """
    pass
