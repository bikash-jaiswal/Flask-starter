from flask import Flask


def create_app():
    app = Flask(__name__)

    # Application configuration
    app.config['SECRET_KEY'] = 'your-secret-key'

    # Register routes
    from . import routes
    app.register_blueprint(routes.bp)

    return app