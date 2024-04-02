from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from .config import Config

# Instantiate extensions
db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
jwt = JWTManager()


def create_app(config_class=Config):
    app = Flask('e-note-api')
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    jwt.init_app(app)

    # Register blueprints
    from app.route import bp as routes_bp
    app.register_blueprint(routes_bp)

    # Other setup can go here
    app.config['WTF_CSRF_ENABLED'] = False

    return app
