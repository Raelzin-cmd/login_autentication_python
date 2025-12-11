from flask import make_response, request
from database import users_repository
from jwt import decode, ExpiredSignatureError


def middleware():
    # Libera as rotas públicas que não precisam de autenticação
    if request.path in ['/register', '/login']:
        return None
    
    # Obtém o header Authorization
    bearerToken = request.headers.get('authorization')

    # Verifica se o token foi enviado
    if bearerToken == None:
        return make_response({'message': 'Token not informed'}, 401)
    
    # Remove o prefixo "Bearer " para ficar apenas com o token JWT
    token = bearerToken.replace('Bearer ', '')

    try:
        # Decodifica o token usando a chave secreta e o algoritmo HS256
        dataUser = decode(token, 'secretPass', algorithms=['HS256'])

        # Busca o usuário no banco usando o ID presente no token
        user = users_repository.find(dataUser['id'])

        # Se o usuário não existir mais, bloqueia o acesso
        if user == None:
            return make_response({'message': 'Unauthorized'}, 401)
        
        # Anexa o usuário ao request para ser usado pelos controllers
        request.user = user

        # Libera a requisição para continuar
        return
    
    except ExpiredSignatureError:
        # Caso o token já esteja expirado
        return make_response({'message': 'Token expired'}, 401)