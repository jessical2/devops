from email.policy import default
from flask_login import UserMixin
from . import db
# from werkzeug.security import generate_password_hash, check_password_hash

class CustomUserMixin(UserMixin): 
    @property
    def is_admin(self):
        return bool(self.admin)

# Create tables
class User(CustomUserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(200), primary_key=False, unique=False, nullable=False)
    admin = db.Column(db.Boolean, unique=False, nullable=False)

# class Room(db.Model):
#     __tablename__ = 'room'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(15), unique=False, nullable=False)
#     capacity = db.Column(db.Integer, unique=False, nullable=False)
#     available_from = db.Column(db.Time, unique=True, nullable=False) #TODO Check DONT THINK NEEDED
#     available_to = db.Column(db.Time, unique=True, nullable=False) #TODO Check DONT THINK NEEDED

# class Booking(db.Model):
#     __tablename__ = 'booking'
#     id = db.Column(db.Integer, primary_key=True)
#     start_time = db.Column(db.Integer, nullable=False)
#     end_time = db.Column(db.Integer, nullable=False) #TODO Can be calculated or duration?
#     date = db.Column(db.DateTime, nullable=False)
#     duration = db.Column(db.Integer, nullable=False) #TODO Add function
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)


