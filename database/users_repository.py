from database.connection import cursor, connect
from bcrypt import hashpw, gensalt  


def registerUser(name, email, password):
    # Gera o hash da senha usando bcrypt e um salt aleatório
    pass_hash = hashpw(str.encode(password), gensalt())

    # Insere o usuário no banco e retorna todos os campos inseridos
    result = cursor.execute(
        'INSERT INTO users (name, email, password) VALUES (%s, %s, %s) RETURNING *',
        (name, email, pass_hash.decode())
    )

    # Confirma a transação no banco
    connect.commit()

    # Obtém a linha retornada pelo banco de dados
    user = result.fetchone()

    # Retorna o usuário como dicionário
    return {
        'id': user[0],
        'name': user[1],
        'email': user[2],
        'password': user[3]
    }


def findEmail(email):
    # Busca o usuário pelo email informado
    result = cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
    user = result.fetchone()

    # Se não houver usuário, retorna None
    if (user == None):
        return None
    
    # Caso exista, retorna o usuário como dicionário
    return {
        'id': user[0],
        'name': user[1],
        'email': user[2],
        'password': user[3]
    }


def find(id):
    # Busca o usuário pelo ID informado
    result = cursor.execute('SELECT * FROM users WHERE id = %s', (id,))
    user = result.fetchone()

    # Se não houver usuário, retorna None
    if (user == None):
        return None
    
    # Caso exista, retorna o usuário como dicionário
    return {
        'id': user[0],
        'name': user[1],
        'email': user[2],
        'password': user[3]
    }