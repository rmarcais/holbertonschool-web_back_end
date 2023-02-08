#!/usr/bin/env python3
""" Main 5
"""
import uuid
from api.v1.auth.basic_auth import BasicAuth
from models.user import User

""" Create a user test """
user_email = str(uuid.uuid4())
user_clear_pwd = str(uuid.uuid4())
user = User()
user.email = user_email
user.first_name = "Bob"
user.last_name = "Dylan"
user.password = user_clear_pwd
print("New user: {}".format(user.display_name()))
user.save()

user_email2 = str(uuid.uuid4())
user_clear_pwd2 = str(uuid.uuid4())
user2 = User()
user2.email = user_email
user2.first_name = "Bob"
user2.last_name = "Dylan"
user2.password = user_clear_pwd
print("New user: {}".format(user2.display_name()))
user2.save()

""" Retreive this user via the class BasicAuth """

a = BasicAuth()

b = a.user_object_from_credentials("hello", user_clear_pwd)
print(b.display_name() if b is not None else "None")
