from flask import Flask
from controllers import users, login
from middlewares import middleware

app = Flask(__name__)

app.before_request(middleware.middleware)

app.add_url_rule('/register', methods=['POST'], view_func=users.registerUser)
app.add_url_rule('/login', methods=['POST'], view_func=login.login)
app.add_url_rule('/user', methods=['GET'], view_func=users.user)


app.run(port=3000, debug=True)