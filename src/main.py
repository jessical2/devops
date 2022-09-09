from flask import Blueprint, render_template, redirect, url_for
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

@main.route('/booking', methods=['POST'])
def booking_post():
    return redirect(url_for('main.booked'))

@main.route('/booked')
def booked():
    return render_template('booked.html')

@main.route('/admin')
def admin():
    return render_template('admin.html')

