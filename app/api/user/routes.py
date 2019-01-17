from flask import request
from flask_jwt_extended import jwt_required

from app.utils import Response
from app.decorators import token_required, admin_token_required

from . import controller
from . import user_blp


@user_blp.route("/save_new_uer", methods=['GET', 'POST'])
def save_new_uer():
    if not request.json:
        return Response.bad_request()
    
    return controller.save_new_uer(data=request.json)


@user_blp.route("/get_all_users", methods=['GET', 'POST'])
@admin_token_required
def get_all_users():
    return controller.get_all_users()
    

@user_blp.route("/get_a_user/<id>", methods=['GET', 'POST'])
@admin_token_required
def get_a_user(id):
    return controller.get_a_user(id)


@user_blp.route("/delete_user/<public_id>", methods=['GET', 'POST'])
@admin_token_required
def delete_user(public_id):
    return controller.delete_user_by_public_id(public_id)