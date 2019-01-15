from flask import request
from app.utils import Response
from . import controller

from . import auth_blp

@auth_blp.route("/login", methods=['GET', 'POST'])
def user_login():
    post_data = request.json
    print("post_data: ", post_data)
    return controller.Auth.login_user(data=post_data)
