import uuid
import datetime
from flask import json
from app.models import User,db
from app.utils import Response
from ... import constants
from . import controller 


def save_new_uer(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            username=data['username'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow(),
            admin=data['admin']
        )
        save_changes(new_user)
        return generate_token(new_user)
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists.'
        }
        return Response.jsonify(message=response_object)
        
def get_all_users():
    user_list = User.query.all()
    if not user_list:
        return Response.bad_request()
    else:
        user_list = User.query.all()
    
    output = [user.to_json() for user in user_list]
    return Response.jsonify(data=output)
    
def get_a_user(id):
    user = User.query.filter_by(id=id).first()
    if not user:
        return Response.bad_request(message=constants.MESG_USER_NOT_FOUND)
    user = User.query.filter_by(id=id).first().to_json()
    return Response.jsonify(data=user) 

def delete_user_by_public_id(public_id):
    user = User.query.filter_by(public_id=public_id).first()
    if not user:
        return Response.bad_request(message=constants.MESG_USER_NOT_FOUND)

    db.session.delete(user)
    db.session.commit()
    return Response.jsonify("OK", "User is deleted.")

def generate_token(user):
    try:
        # generate the auth token
        auth_token = User.encode_auth_token(user.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return Response.jsonify(message=response_object)
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return Response.jsonify(message=response_object)

def save_changes(data):
    db.session.add(data)
    db.session.commit()
