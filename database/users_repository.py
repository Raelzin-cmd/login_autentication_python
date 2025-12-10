from database.connection import cursor, connect
from bcrypt import hashpw, gensalt  

def registerUser(name, email, password):
    pass_hash = hashpw(str.encode(password), gensalt())
    result = cursor.execute(
        'INSERT INTO users (name, email, password) VALUES (%s, %s, %s) RETURNING *',
        (name, email, pass_hash)
    )
    connect.commit()
    user = result.fetchone()
    return {
        'id': user[0],
        'name': user[1],
        'email': user[2],
        'password': user[3],
    }