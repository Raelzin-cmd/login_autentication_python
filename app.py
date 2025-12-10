from flask import Flask
from controllers import users

app = Flask(__name__)

app.add_url_rule('/register', methods=['POST'], view_func=users.registerUser)

app.run(port=3000, debug=True)