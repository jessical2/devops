from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('home.html')

@main.route('/booking')
@login_required
def booking():
    return render_template('booking.html')

@main.route('/booked')
def booked():
    return ('Booked')

