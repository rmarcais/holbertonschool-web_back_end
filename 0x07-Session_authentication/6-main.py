#!/usr/bin/env python3
""" Main 6
"""
import base64
from api.v1.auth.basic_auth import BasicAuth
from models.user import User

""" Create a user test """
user_email = "bob@hbtn.io"
user_clear_pwd = "H0lbertonSchool98!"
user = User()
user.email = user_email
user.password = user_clear_pwd
print("New user: {} / {}".format(user.id, user.display_name()))
user.save()

user_email2 = "bob@hbtn.com"
user_clear_pwd2 = "helloworld"
user2 = User()
user2.email = user_email2
user2.password = user_clear_pwd2
print("New user: {} / {}".format(user2.id, user2.display_name()))
user2.save()

basic_clear = "{}:{}".format(user_email, user_clear_pwd)
print("Basic Base64: {}".format(base64.b64encode(basic_clear.encode('utf-8')).decode("utf-8")))

basic_clear = "{}:{}".format(user_email2, user_clear_pwd2)
print("Basic Base64: {}".format(base64.b64encode(basic_clear.encode('utf-8')).decode("utf-8")))
