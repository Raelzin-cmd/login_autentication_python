from flask import Flask

app = Flask(__name__)

@app.route('/')

def test():
    return 'hello'

app.run(port=3000, debug=True)