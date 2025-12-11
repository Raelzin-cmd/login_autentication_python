from flask import make_response, request
from database import users_repository
from jwt import decode, ExpiredSignatureError

def middleware():
    if request.path in ['/register', '/login']:
        return None
    
    bearerToken = request.headers.get('authorization')

    if bearerToken == None:
        return make_response({'message': 'Token not informed'}, 401)
    
    token = bearerToken.replace('Bearer ', '')

    try:
        dataUser = decode(token, 'secretPass', algorithms=['HS256'])
        user = users_repository.find(dataUser['id'])

        if user == None:
            return make_response({'message': 'Unauthorized'}, 401)
        
        request.user = user

        return
    
    except ExpiredSignatureError:
        return make_response({'message': 'Token expired'}, 401)