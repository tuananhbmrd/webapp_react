from flask import request
from app.utils import Response
from . import controller

from . import auth_blp

@auth_blp.route("/login", methods=['GET', 'POST'])
def user_login():
    if not request:
        return Response.bad_request()
    post_data = request.json
    return controller.Auth.login_user(data=post_data)


@auth_blp.route("/logout", methods=['GET', 'POST'])
def user_logout():
    auth_header = request.headers.get('Authorization')
    return controller.Auth.logout_user(data=auth_header)