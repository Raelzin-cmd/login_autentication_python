from flask import Flask
from controllers import users, login
from middlewares import middleware


# Cria a instância principal de aplicação Flask
app = Flask(__name__)

# Executa o middleware antes de qualquer requisição
app.before_request(middleware.middleware)

# Rota para registrar um novo usuário (POST)
app.add_url_rule('/register', methods=['POST'], view_func=users.registerUser)
# Rota para login e geração de token JWT (POST)
app.add_url_rule('/login', methods=['POST'], view_func=login.login)
# Rota protegida que retorna o usuário autenticado (GET)
app.add_url_rule('/user', methods=['GET'], view_func=users.user)

# Inicia o servidor na porta 3000 com debug ativado
app.run(port=3000, debug=True)