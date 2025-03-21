from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('config.py')

    db.init_app(app)
    jwt.init_app(app)

    from .api import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app