
from flask import Flask, abort, render_template, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from .limiter import limiter

from functools import wraps

from werkzeug.security import generate_password_hash

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    from .models import User

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

   
    db.init_app(app)

    # Initialise flask-limiter, apply across the application
    limiter.init_app(app)

    with app.app_context():
        # blueprint for auth routes
        from .auth import auth as auth_blueprint
        app.register_blueprint(auth_blueprint)

        # blueprint for main
        from .main import main as main_blueprint
        app.register_blueprint(main_blueprint)

        # blueprint for admin
        from .admin import admin as admin_blueprint
        app.register_blueprint(admin_blueprint)

        # blueprint for bookings
        from .bookings import bookings as bookings_blueprint
        app.register_blueprint(bookings_blueprint)

        db.create_all()

        checkUsers = User.query.filter_by(id='1').first()
        if not checkUsers:
            populate_demo_users()
        
        login_manager = LoginManager()
        login_manager.login_view = 'auth.login'
        login_manager.init_app(app)

        @login_manager.user_loader
        def load_user(user_id):
            return User.query.get(int(user_id))

        return app


def populate_demo_users():
    from .models import User

    password1= generate_password_hash('Admin', method='sha256')
    password2= generate_password_hash('User', method='sha256')
    db.session.add_all(
        [
            User(email="admin@admin.com", name="Admin", password=password1, admin=True),
            User(email="user@user.com", name="User", password=password2, admin=False)
        ]
    )
    db.session.commit()


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_admin:
            abort(403)
        return f(*args, **kwargs)
    return decorated_function