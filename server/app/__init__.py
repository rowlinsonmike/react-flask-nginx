from flask import Flask


def create_app(config):
    app = Flask(__name__)

    from app.routes.hello import hello
    app.register_blueprint(hello(), url_prefix='/api/hello')

    
    return app