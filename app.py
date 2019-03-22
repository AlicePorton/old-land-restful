from flask import Flask

# app = Flask(__name__)
from app import create_app

app = create_app()

# @app.route('/')
# def hello_world():
#     return 'Hello World!'


if __name__ == '__main__':
    """
    设置port在pycharm中无效
    """
    app.run(debug=True, port=3002)
