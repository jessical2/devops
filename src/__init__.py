from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
    # app = Flask(__name__, instance_relative_config=False)

    # # Application Configuration
    # app.config.from_object('config.Config')

    # # Initialize Plugins
    # db.init_app(app)
    # login_manager.init_app(app)

    # with app.app_context():
    #     from . import routes
    #     from . import auth
    #     from .assets import compile_assets

    #     # Register Blueprints
    #     app.register_blueprint(routes.main_bp)
    #     app.register_blueprint(auth.auth_bp)

    #     # Create Database Models
    #     db.create_all()

    #     # Compile static assets
    #     if app.config['FLASK_ENV'] == 'development':
    #         compile_assets(app)

    #     return app