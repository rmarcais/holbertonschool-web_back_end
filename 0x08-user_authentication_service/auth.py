#!/usr/bin/env python3
"""auth module
"""

import bcrypt
import uuid
from db import DB
from typing import TypeVar
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """Returns the hashed password"""
    bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)

    return hash


def _generate_uuid() -> str:
    """Returns a string representation of a new UUID"""
    return str(uuid.uuid1())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> TypeVar("User"):
        """Registers a new user"""
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(user.email))
        except NoResultFound:
            pass

        hashed_password = _hash_password(password).decode()
        user = self._db.add_user(email, hashed_password)
        return user

    def valid_login(self, email: str, password: bytes) -> bool:
        """
        Checks the password. If it matches,
        return True (False otherwise).
        """
        try:
            user = self._db.find_user_by(email=email)
            password = password.encode("utf-8")
            user_password = user.hashed_password.encode("utf-8")
            return bcrypt.checkpw(password, user_password)
        except NoResultFound:
            return False
