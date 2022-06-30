<<<<<<< HEAD
import jwt
import datetime
from rest_framework.exceptions import AuthenticationFailed


def create_access_token(id):
    return jwt.encode({
        'user_id': id,
        'exp': datetime.datetime.utcnow()+datetime.timedelta(seconds=60),
        'iat': datetime.datetime.utcnow()
    }, 'access_secret', algorithm='HS256')


def decode_access_token(token):
    try:
        payload = jwt.decode(token, 'access_secret', algorithms='HS256')
        return payload['user_id']

    except:
        raise(AuthenticationFailed('Unauthenticated!'))


def create_refresh_token(id):
    return jwt.encode({
        'user_id': id,
        'exp': datetime.datetime.utcnow()+datetime.timedelta(days=7),
        'iat': datetime.datetime.utcnow()
    }, 'refresh_secret', algorithm='HS256')


def decode_refresh_token(token):
    try:
        payload = jwt.decode(token, 'refresh_secret', algorithms='HS256')
        return payload['user_id']

    except:
        raise(AuthenticationFailed('Unauthenticated!'))
=======
import jwt,datetime
from rest_framework.exceptions import AuthenticationFailed

def create_access_token(id):
    return jwt.encode({
        'user_id':id,
        'exp': datetime.datetime.utcnow()+datetime.timedelta(seconds=60),
        'iat': datetime.datetime.utcnow()
    },'access_secret',algorithm='HS256')

def decode_access_token(token):
    try:
        payload = jwt.decode(token,'access_secret',algorithms='HS256')
        return payload['user_id']
    
    except:
        raise(AuthenticationFailed('Unauthenticated!'))
   
def create_refresh_token(id):
    return jwt.encode({
        'user_id':id,
        'exp': datetime.datetime.utcnow()+datetime.timedelta(days=7),
        'iat': datetime.datetime.utcnow()
    },'refresh_secret',algorithm='HS256')
    
def decode_refresh_token(token):
    try:
        payload = jwt.decode(token,'refresh_secret',algorithms='HS256')
        return payload['user_id']
    
    except:
        raise(AuthenticationFailed('Unauthenticated!'))
>>>>>>> e70c3e4ced59f551765d67f6bfaad0f3d15bea86
