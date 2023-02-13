#!/usr/bin/env python3
"""Route module for the API
"""

from flask import Flask, jsonify, request
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
