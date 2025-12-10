from flask import make_response, jsonify, request
from database import users_repository
from bcrypt import checkpw
from jwt import encode
from datetime import datetime, timedelta, timezone

def login():
    body = request.get_json()

    email = body['email']
    password = body['password']

    user = users_repository.findEmail(email)

    if user == None:
        return make_response({'message': 'Access invalid'}, 400)
    
    correctPass = checkpw(str.encode(password), str.encode(user['password']))

    if not correctPass:
        return make_response({'message': 'Access invalid'}, 400)
    
    expire = datetime.now(tz=timezone.utc) + timedelta(hours=8)

    token = encode({'id': user['id'], 'exp': expire}, 'secretPass', 'HS256')

    result = {
        'user': user,
        'token': token
    }

    return make_response(jsonify(result), 200)