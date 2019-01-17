from ...models import User, db
from app.utils import Response
from app.models import BlacklistToken

class Auth:
    
    @staticmethod
    def login_user(data):
        try:
            # fetch the user data
            user = User.query.filter_by(email=data.get('email')).first()
            print("user: ", user)
            print("check: ", user.check_password(data.get('password')))
            if user and user.check_password(data.get('password')):
                auth_token = User.encode_auth_token(user.id)
                if auth_token:
                    response_object = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'Authorization': auth_token.decode()
                    }
                    
                    # mark the token as blacklisted
                    save_token(token=auth_token)
                    return Response.jsonify(message=response_object)
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'email or password does not match.'
                }
                return Response.jsonify(status=401, message=response_object)
                
        except Exception as e:
            response_object = {
                'status': 'fail',
                'message': 'Try again'
            }
            return Response.jsonify(message=response_object)
    
    @staticmethod
    def logout_user(data):
        if data:
            auth_token = data.split(" ")[0]
        else:
            auth_token = ''
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                return
            else:
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return Response.jsonify(status=401, message=response_object)
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return Response.jsonify(status=403, message=response_object)

    @staticmethod
    def get_logged_in_user(new_request):
        # get the auth token
        auth_token = new_request.headers.get('Authorization')
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                user = User.query.filter_by(id=resp).first()
                response_object = {
                    'status': 'success',
                    'data': {
                        'user_id': user.id,
                        'email': user.email,
                        'admin': user.admin,
                        'registered_on': str(user.registered_on)
                    }
                }
                return response_object, 200
            response_object = {
                'status': 'fail',
                'message': resp
            }
            return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 401

def save_token(token):
    blacklist_token = BlacklistToken(token=token)
    try:
        # insert the token
        db.session.add(blacklist_token)
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Successfully logged out.'
        }
        return Response.jsonify(status=200, message=response_object)
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': e
        }
        return Response.jsonify(status=200, message=response_object)


        