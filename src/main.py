from flask import Blueprint, render_template
from . import db

main = Blueprint('main', __name__)


# Routes might have to be changed
@main.route('/')
def booking():
    return render_template('booking.html')

@main.route('/booked')
def booked():
    return ('Booked')

