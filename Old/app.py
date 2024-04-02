from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
# from routes import main as main_blueprint

# Initialize the extensions but without any app instance
jwt = JWTManager()

# Initialize the extensions but without any app instance
db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask('e-note-api')

    # Configure the SQLAlchemy part
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///api_db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Setup the Flask-JWT-Extended extension
    app.config['JWT_SECRET_KEY'] = 'M*$X])us"nv"Q)OTbC{"WCBvXRV0+e'  # Change this to a random secret key
    jwt.init_app(app)

    # Initialize the app with the extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints
    # app.register_blueprint(main_blueprint)

    return app
