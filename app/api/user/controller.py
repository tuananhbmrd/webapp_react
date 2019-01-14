import uuid
import datetime
from flask import json
from app.models import User,db
from app.utils import Response
from . import controller 


def save_new_uer(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            username=data['username'],
            password_hash=data['password_hash'],
            registered_on=datetime.datetime.utcnow()
        )
        print(new_user)
        save_changes(new_user)
        return Response.jsonify(data=new_user.to_json())
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists.'
        }
        return Response.jsonify(message=response_object)

def delete_user_by_public_id(public_id):
    user = User.query.filter_by(public_id=public_id).first()
    if not user:
        response_object = {
            'status': 'fail',
            'message': 'User does not exist.'
        }
        return Response.bad_request()

    db.session.delete(user)
    db.session.commit()

    return Response.jsonify("OK", "User is deleted.")

def get_all_users():
    user_list = User.query.all()
    if not user_list:
        return Response.bad_request()
    return User.query.all()

def get_a_user(id):
    user = User.query.filter_by(id=id).first()
    if not user:
        Response.bad_request()
    else:
        return Response.jsonify(data=User.query.filter_by(id=id).first().to_json()) 

def save_changes(data):
    db.session.add(data)
    db.session.commit()
