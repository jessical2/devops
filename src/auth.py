from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
import re
from .limiter import limiter
from password_strength import PasswordPolicy


auth = Blueprint('auth', __name__)

password_policy = PasswordPolicy.from_names(
    length=8,
    uppercase=1,
    numbers=1,
    special=1,
    nonletters=1
)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    # User can log in with the parameters below
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # Check if the user actually exists
    # Take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # If the user doesn't exist or password is wrong, reload the page

    # If the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('bookings.book_page'))

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    # User signs up and inserts the below information
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    
    if email_validator(email) == False:
        flash('Email contains unaccepted characters')
        return redirect(url_for('auth.signup'))
    
    if name_validator(name) == False:
        flash('Name contains unaccepted characters')
        return redirect(url_for('auth.signup'))

    # If this returns a user, then the email already exists in database
    user = User.query.filter_by(email=email).first() 

    # If a user is found, redirect back to signup page so user can try again
    if user: 
        flash('Email address already exists. Use a different email or login')
        return redirect(url_for('auth.signup'))
    
    if email == "" or name == "" or password == "":
        flash('Please input all fields and try again')
        return redirect(url_for('auth.signup'))

    # Test password strength
    if password_validator(password) == False:
        flash("Password is not strong enough. Passwords must be at least 8 characters and contain a capital letter, number, and special character")
        return redirect(url_for('auth.signup'))


    # Create a new user with the form data. Hash the password.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'), admin=False)

    # Add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


# Validate emails input
def email_validator(email):
    # Check emails contain no special characters other than @ and .
    if not re.match("^[A-Za-z0-9@.]+$", email):
        return False
    return True

# Validate name input
def name_validator(name):
    # Check name contains no special characters
    if not re.match("^([A-Za-z0-9]+$)", name): 
        return False
    return True   


def password_validator(password):
    # Test password strength
    validate_password = password_policy.test(password)
    if len(validate_password) != 0:
        return False
    return True



