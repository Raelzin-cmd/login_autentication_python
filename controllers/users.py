from flask import make_response, jsonify, request
from database import users_repository
from jwt import decode, ExpiredSignatureError

def registerUser():
    body = request.get_json()

    existEmail = users_repository.findEmail(body['email'])

    if (existEmail != None):
        return make_response({'message': 'User already exists'}, 400)
    
    user = users_repository.registerUser(body['name'], body['email'], body['password'])

    return make_response(jsonify(user), 201)

def testAuthentication():
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

        return f'{user['name']} successfully authenticated'
    
    except ExpiredSignatureError:
        return make_response({'message': 'Token expired'}, 401)