import click
from flask import Flask
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from werkzeug.security import generate_password_hash

db = SQLAlchemy()
login_manager = LoginManager()

@click.command
@with_appcontext
def seed():
    from .models import User
    new_admin = User(email='admin@admin.com', name='Admin', password=generate_password_hash('Admin', method='sha256'), admin=True)

    # add the new user to the database
    db.session.add(new_admin)
    db.session.commit()

def create_app():
    app = Flask(__name__)

    from .models import User

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # with app.app_context():
    #     # creating an initial admin user
    #     new_admin = db.User(email='admin@admin.com', name='Admin', password=generate_password_hash('Admin', method='sha256'), admin=True)

    #     # add the new user to the database
    #     db.session.add(new_admin)
    #     db.session.commit()

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    app.cli.add_command(seed)

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