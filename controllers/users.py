from flask import make_response, jsonify, request
from database import users_repository
from jwt import decode, ExpiredSignatureError


def registerUser():
    # Obtém o corpo JSON enviado na requisição
    body = request.get_json()

    # Verifica se já existe um usuário com o email informado
    existEmail = users_repository.findEmail(body['email'])

    # Caso o email já esteja cadastrado, retorna erro
    if (existEmail != None):
        return make_response({'message': 'User already exists'}, 400)
    
    # Cria um novo usuário no repositório com nome, email e senha
    user = users_repository.registerUser(body['name'], body['email'], body['password'])

    # Retorna o usuário recém-criado com status de criado (201)
    return make_response(jsonify(user), 201)


def user():
    # Retorna os dados do usuário já anexados ao request (via middleware / token)
    return make_response(jsonify(request.user), 200)