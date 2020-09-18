import logging
# flask packages
from flask import Flask, app
from flask_restful import Api
from flask_mongoengine import MongoEngine
# cors
from flask_cors import CORS
# flask socket io
from flask_socketio import SocketIO

# local packages
from backend.src.api.routes import create_routes
# default mongodb configuration
from backend.src.api.socket import RoomSocket

default_config = {'MONGODB_SETTINGS': {
    'db': 'test_db',
    'host': 'localhost',
    'port': 27017,
    'username': 'admin',
    'password': 'password',
    'authentication_source': 'admin'}}


def get_flask_app(config: dict = None) -> app.Flask:
    """
    Initializes Flask app with given configuration.
    Main entry point for wsgi (gunicorn) server.
    :param config: Configuration dictionary
    :return: app
    """
    # init flask
    flask_app = Flask(__name__)

    # configure app
    config = default_config if config is None else config
    flask_app.config.update(config)
    # init api and routes
    api = Api(app=flask_app)
    create_routes(api=api)
    # init mongoengine
    db = MongoEngine(app=flask_app)

    # enable CORS
    CORS(flask_app, resources={r'/*': {'origins': '*'}})

    return flask_app


if __name__ == '__main__':
    # Main entry point when run in stand-alone mode.
    app = get_flask_app()
    logging.basicConfig(level=logging.DEBUG)
    socketio = SocketIO(app, cors_allowed_origins='*')
    socketio.on_namespace(RoomSocket('/rooms/'))
    socketio.run(app, debug=True)
