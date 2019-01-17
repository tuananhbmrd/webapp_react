from functools import wraps
from flask import request

from .utils import Response

from app.api.auth.controller import Auth


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        
        data, status = Auth.get_logged_in_user(request)
        token = data.get('data')
        if not token:
            return Response.jsonify(status=status, message=data)
            
        return f(*args, **kwargs)

    return decorated

def admin_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        data, status = Auth.get_logged_in_user(request)
        print("data: ", data)
        token = data.get('data')
        print("token: ", token)

        if not token:
            return Response.jsonify(status=status, message=data)

        admin = token.get('admin')
        if not admin:
            response_object = {
                'status': 'fail',
                'message': 'admin token required'
            }
            return Response.jsonify(status=status, message=response_object)
        
        return f(*args, **kwargs)
    return decorated
