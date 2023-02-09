#!/usr/bin/env python3
""" session_db_auth module containing the SessionExpAuth class """

from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
import os


class SessionDBAuth(SessionExpAuth):
    """SessionDBAuth class"""

    def create_session(self, user_id: str = None) -> str:
        """Creates a Session ID for a user_id"""
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        user_session = UserSession()
        user_session.user_id = user_id
        user_session.session_id = session_id
        user_session.save()

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns a User ID based on a Session ID"""
        print("lalala")
        if not session_id:
            return None
        for item in UserSession.all():
            if item.session_id == session_id:
                return item.user_id

    def destroy_session(self, request=None) -> bool:
        """Deletes the user session / logouts"""
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if not session_id:
            return False

        user_id = self.user_id_for_session_id(session_id)
        if not user_id:
            return False

        for item in UserSession.all():
            if item.session_id == session_id:
                item.remove()
                break

        return True
