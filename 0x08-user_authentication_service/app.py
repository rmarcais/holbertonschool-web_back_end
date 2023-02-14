#!/usr/bin/env python3
"""Route module for the API
"""

from flask import Flask, abort, jsonify, request, redirect
from auth import Auth

app = Flask(__name__)

auth = Auth()


@app.route('/')
def welcome() -> str:
    """Says weclome !"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=["POST"], strict_slashes=False)
def users() -> str:
    """End-point to register a user"""
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        auth.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    return jsonify({"email": "{}".format(email), "message": "user created"})


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """login function"""
    email = request.form.get("email")
    password = request.form.get("password")

    if auth.valid_login(email, password):
        session_id = auth.create_session(email)
        res = jsonify({"email": "{}".format(email), "message": "logged in"})
        res.set_cookie("session_id", session_id)
        return res
    else:
        abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout() -> str:
    """logout function"""
    session_id = request.cookies.get("session_id")
    try:
        user = auth.get_user_from_session_id(session_id)
        auth.destroy_session(user.id)
        return redirect("/", 301)
    except Exception:
        abort(403)


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile() -> str:
    """profile function to respond to the GET /profile route"""
    session_id = request.cookies.get("session_id")
    user = auth.get_user_from_session_id(session_id)
    if not user:
        abort(403)
    return jsonify({"email": "{}".format(user.email)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
