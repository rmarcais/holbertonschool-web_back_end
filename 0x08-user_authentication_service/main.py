#!/usr/bin/env python3
"""main module
"""

import requests

EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


def register_user(email: str, password: str) -> None:
    """Tests the users end-point"""
    data = {"email": email, "password": PASSWD}
    r = requests.post("http://localhost:5000/users", data=data)

    assert r.status_code == 200
    assert r.json() == {"email": "guillaume@holberton.io",
                        "message": "user created"}


def log_in_wrong_password(email: str, password: str) -> None:
    """Tests the sessions end-point"""
    data = {"email": email, "password": password}
    r = requests.post("http://localhost:5000/sessions", data=data)

    assert r.status_code == 401


def log_in(email: str, password: str) -> str:
    """Tests the sessions end-point"""
    data = {"email": email, "password": password}
    r = requests.post("http://localhost:5000/sessions", data=data)

    assert r.status_code == 200
    assert r.json() == {"email": email, "message": "logged in"}

    return r.cookies.get("session_id")


def profile_unlogged() -> None:
    """Tests the profile end-point"""
    r = requests.get("http://localhost:5000/profile")

    assert r.status_code == 403


def profile_logged(session_id: str) -> None:
    """Tests the profile end-point"""
    cookies = {"session_id": session_id}
    r = requests.get("http://localhost:5000/profile", cookies=cookies)

    assert r.status_code == 200
    json_dict = r.json()
    email_json = json_dict.get("email")
    assert json_dict == {"email": email_json}


def log_out(session_id: str) -> None:
    """Tests the session end-point"""
    cookies = {"session_id": session_id}
    r = requests.delete("http://localhost:5000/sessions", cookies=cookies,
                        allow_redirects=False)

    assert r.status_code == 302


def reset_password_token(email: str) -> str:
    """Tests the reset_password end-point"""
    data = {"email": email}
    r = requests.post("http://localhost:5000/reset_password", data=data)

    assert r.status_code == 200
    json_dict = r.json()
    reset_token = json_dict.get("reset_token")
    assert json_dict == {"email": email, "reset_token": reset_token}

    return reset_token


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Tests the reset_password end-point"""
    data = {"email": email,
            "reset_token": reset_token,
            "new_password": new_password}
    r = requests.put("http://localhost:5000/reset_password", data=data)

    assert r.status_code == 200
    assert r.json() == {"email": email, "message": "Password updated"}


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
