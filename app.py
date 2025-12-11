from flask import Flask
from controllers import users, login

app = Flask(__name__)

app.add_url_rule('/register', methods=['POST'], view_func=users.registerUser)
app.add_url_rule('/login', methods=['POST'], view_func=login.login)
app.add_url_rule('/test', methods=['GET'], view_func=users.testAuthentication)


app.run(port=3000, debug=True)