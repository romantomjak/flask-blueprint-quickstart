from flask import Flask


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)

    register_blueprints(app)

    return app


def register_blueprints(app):
    import polls

    app.register_blueprint(polls.blueprint, url_prefix='/polls')
