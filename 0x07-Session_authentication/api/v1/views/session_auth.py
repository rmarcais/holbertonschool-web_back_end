#!/usr/bin/env python3
""" Module of auth_session views
"""

from api.v1.views import app_views
from flask import abort, jsonify, request
from api.v1.auth.session_auth import SessionAuth
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """
    POST /auth_session/login
    Returns the dictionary representation of the User
    or error status code if the user can't be found
    """
    email = request.form.get("email")
    if not email or email == "":
        return jsonify({"error": "email missing"}), 400

    password = request.form.get("password")
    if not password or password == "":
        return jsonify({"error": "password missing"}), 400

    user_list = User.search({"email": email})
    if not user_list:
        return jsonify({"error": "no user found for this email"}), 404

    user = user_list[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    auth = SessionAuth()
    session_id = auth.create_session(user.id)
    cookie_name = os.getenv("SESSION_NAME")
    response = jsonify(user.to_json())
    response.set_cookie(cookie_name, session_id)

    return response
