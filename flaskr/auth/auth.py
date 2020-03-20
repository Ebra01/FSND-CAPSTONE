import os
import json
from flask import request
from flask_login import current_user
from functools import wraps
from jose import jwt
from urllib.request import urlopen
from flaskr.models.models import JWT

AUTH0_DOMAIN = os.getenv('DOMAIN')
ALGORITHMS = ['RS256']
API_AUDIENCE = os.getenv('AUDIENCE')

# AuthError Exception
'''
AuthError Exception
A standardized way to communicate auth failure modes
'''


class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


def autherrorhandler(error, default_message):
    """
    Here we handle error's code, message,
     and status to then send it to errors/handlers.py
    """

    try:
        return error['description'], error['code']
    except TypeError:
        return default_message


# Auth Header

def get_token_auth_header():
    """
    Check if the request header
    (Content-Type) is {application/json}.

    If Content-Type = application/json,
    we request and return data as JSON objects.

    If Content-Type != application/json,
    we use JWT Table to get current user' access_token by their id.

    """

    content_type = request.headers.get('Content-Type')

    if content_type == 'application/json':

        auth = request.headers.get('Authorization', None)
        if not auth:
            raise AuthError({
                'code': 'Authorization Header Missing',
                'description': 'Authorization header is expected.'
            }, 401)

        parts = auth.split()
        if parts[0].lower() != 'bearer':
            raise AuthError({
                'code': 'Invalid Header',
                'description': 'Authorization header'
                               ' must start with "Bearer".'
            }, 401)

        elif len(parts) == 1:
            raise AuthError({
                'code': 'Invalid Header',
                'description': 'Token not found.'
            }, 401)

        elif len(parts) > 2:
            raise AuthError({
                'code': 'Invalid Header',
                'description': 'Authorization header'
                               ' must be bearer token.'
            }, 401)

        token = parts[1]
        return token
    else:
        try:
            # Here we get the token from JWT Table by giving current_user's id
            token = JWT.query.filter_by(user_id=current_user.id).first()
            token = token.display()
            access_token = token['access_token']
            if access_token:
                return access_token
            else:
                raise AuthError({
                    "code": "Authorization Header Missing",
                    "description":
                        "Authorization header is expected"}, 401)
        except Exception as e:
            print(e)
            raise AuthError({
                "code": "Authorization Header Missing",
                "description":
                    "Authorization header is expected"}, 401)


def check_permissions(permission, payload):
    """
    Check if permissions is in the payload (user's access token)

    if not raise authentication error

    if it instanced we check if this user have
    the required permission to access an endpoint

    """
    if 'permissions' not in payload:
        raise AuthError({
            'code': 'Invalid Claims',
            'description': 'JWT does not include permissions.'
        }, 400)

    if permission not in payload['permissions']:
        raise AuthError({
            'code': 'Unauthorized',
            'description': 'Permission not found'
        }, 403)

    return True


def verify_decode_jwt(token):
    """
    Here we verify the decode jwt using Auth0's logic
    """
    jsonurl = urlopen(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json')
    jwks = json.loads(jsonurl.read())
    unverified_header = jwt.get_unverified_header(token)
    rsa_key = {}
    if 'kid' not in unverified_header:
        raise AuthError({
            'code': 'Invalid Header',
            'description': 'Authorization malformed.'
        }, 401)

    for key in jwks['keys']:
        if key['kid'] == unverified_header['kid']:
            rsa_key = {
                'kty': key['kty'],
                'kid': key['kid'],
                'use': key['use'],
                'n': key['n'],
                'e': key['e']
            }
    if rsa_key:
        try:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer=f'https://{AUTH0_DOMAIN}/'
            )

            return payload

        except jwt.ExpiredSignatureError:
            raise AuthError({
                'code': 'Token Expired',
                'description': 'Token expired.'
            }, 401)

        except jwt.JWTClaimsError:
            raise AuthError({
                'code': 'Invalid Claims',
                'description': 'Incorrect claims. '
                               'Please, check the audience and issuer.'
            }, 401)
        except Exception:
            raise AuthError({
                'code': 'Invalid Header',
                'description': 'Unable to parse authentication token.'
            }, 400)

    # if not rsa_keys
    raise AuthError({
        'code': 'Invalid Header',
        'description': 'Unable to find the appropriate key.'
    }, 400)

    # raise Exception('Not Implemented')


def requires_auth(permission=''):
    """
    Here we have a decorator to request,
    and send permissions and
    check if the user is valid to access a certain endpoint
    """
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = get_token_auth_header()
            try:
                payload = verify_decode_jwt(token)
            except Exception as e:
                print(e)
                raise AuthError({
                    'code': 'Unauthorized',
                    'description': 'Permissions not found'
                }, 401)

            check_permissions(permission, payload)

            return f(payload, *args, **kwargs)

        return wrapper
    return requires_auth_decorator
