#!/usr/bin/env python3
""" session_db_auth module containing the SessionExpAuth class """

from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from typing import TypeVar


class SessionDBAuth(SessionExpAuth):
    """SessionDBAuth class"""

    def create_session(self, user_id: str = None) -> str:
        """Creates a Session ID for a user_id"""
        user_session = UserSession()
        user_session.user_id = user_id
        session_id = super().create_session(user_id)
        user_session.session_id = session_id
        user_session.save()

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns a User ID based on a Session ID"""
        result = super().user_id_for_session_id(session_id)
        return result

    def destroy_session(self, request=None) -> bool:
        """Deletes the user session / logouts"""
        return super().destroy_session(request)
