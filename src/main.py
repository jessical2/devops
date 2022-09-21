from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return redirect(url_for("bookings.book_page"))

