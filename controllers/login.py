from flask import make_response, jsonify, request
from database import users_repository
from bcrypt import checkpw

def login():
    body = request.get_json()

    email = body['email']
    password = body['password']

    user = users_repository.findEmail(email)

    if (user == None):
        return make_response({'message': 'Access invalid'}, 400)
    
    correctPass = checkpw(str.encode(password), str.encode(user['password']))

    if not correctPass:
        return make_response({'message': 'Access invalid'}, 400)
    
    result = {
        'user': user
    }

    return make_response(jsonify(result), 200)