from flask import Flask


def register_blueprints(app):
    """

    :param app:
    :return:
    """
    from app.api import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prifix='/v1')


def register_plugin():
    pass


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')
    register_blueprints(app)
    register_plugin(app)
    return app
