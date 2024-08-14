from flask import Flask


def create_app():
    app = Flask(__name__)

    # Importing all the routes
    from .routes import api

    # Registering all the blueprint
    app.register_blueprint(api)

    # Returning app
    return app
