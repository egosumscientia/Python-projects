from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from .config import Config

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # ⚠️ IMPORTA LOS MODELOS ANTES DE MIGRAR
    from .models import User  # Importa aquí explícitamente

    Migrate(app, db)
    jwt.init_app(app)

    from .routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from .auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app
