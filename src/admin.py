from datetime import datetime
from flask_login import login_required, current_user
from flask import Blueprint, render_template, redirect, url_for, request

from .models import Room, Booking, User
from . import db, admin_required

admin = Blueprint('admin', __name__)

@admin.route('/admin')
@login_required
@admin_required
def admin_page():
    bookings = db.session.query(Booking, Room, User).join(Room, Booking.room_id == Room.id).join(User, Booking.user_id == User.id).all()

    return render_template('admin.html', admin_page=True, bookings=bookings, fromtimestamp=datetime.fromtimestamp, current_user=current_user)


@admin.route('/admin/room', methods=['POST'])
@login_required
@admin_required
def room_post():
    name = request.form.get('name')
    capacity = request.form.get('capacity')

    new_room = Room(name=name, capacity=capacity)

    # Add new room to database
    db.session.add(new_room)
    db.session.commit()
    
    return redirect(url_for('admin.admin_page'))