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

def user():
    return make_response(jsonify(request.user), 200)