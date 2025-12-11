from flask import make_response, jsonify, request
from database import users_repository
from bcrypt import checkpw
from jwt import encode
from datetime import datetime, timedelta, timezone


def login():
    # Obtém o corpo JSON enviado na requisição
    body = request.get_json()

    # Extrai o email e a senha enviados pelo cliente
    email = body['email']
    password = body['password']

    # Busca o usuário pelo email no repositório
    user = users_repository.findEmail(email)

    # Caso o usuário não exista, retorna erro de acesso inválido
    if user == None:
        return make_response({'message': 'Access invalid'}, 400)
    
    # Verifica se a senha informada corresponde ao hash armazenado
    correctPass = checkpw(str.encode(password), str.encode(user['password']))

    # Se a senha estiver incorreta, retorna erro de acesso inválido
    if not correctPass:
        return make_response({'message': 'Access invalid'}, 400)
    
    # Define o tempo de expiração do token (8 horas a partir de agora)
    expire = datetime.now(tz=timezone.utc) + timedelta(hours=8)

    # Gera o token JWT com ID do usuário e data de expiração
    token = encode({'id': user['id'], 'exp': expire}, 'secretPass', 'HS256')

    # Organiza o resultado contendo o usuário e o token
    result = {
        'user': user,
        'token': token
    }

    # Retorna a resposta JSON com status 200 (OK)
    return make_response(jsonify(result), 200)