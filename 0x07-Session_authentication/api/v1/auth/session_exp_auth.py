#!/usr/bin/env python3
""" session_exp_auth module containing the SessionExpAuth class """

from api.v1.auth.session_auth import SessionAuth
from datetime import datetime as d, timedelta
import os


class SessionExpAuth(SessionAuth):
    """SessionExpAuth class"""

    def __init__(self) -> None:
        """Initialization"""
        try:
            self.session_duration = int(os.getenv("SESSION_DURATION"))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id: str = None) -> str:
        """Creates a Session ID for a user_id"""
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        self.user_id_by_session_id[session_id] = {"user_id": user_id,
                                                  "created_at": d.now()}

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns a User ID based on a Session ID"""
        if not session_id:
            return None

        session_dict = self.user_id_by_session_id.get(session_id)
        if not session_dict:
            return None

        user_id = session_dict.get("user_id")
        if self.session_duration <= 0:
            return user_id

        created_at = session_dict.get("created_at")
        if not created_at:
            return None

        exp_date = created_at + timedelta(seconds=self.session_duration)
        if exp_date < d.now():
            return None

        return user_id
