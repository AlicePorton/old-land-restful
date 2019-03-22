from flask import Flask

# app = Flask(__name__)
from app import create_app

app = create_app()

# @app.route('/')
# def hello_world():
#     return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True, port=3001)
