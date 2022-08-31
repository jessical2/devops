from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# Create tables
class User(UserMixin, db.model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(200), primary_key=False, unique=False, nullable=False)

    def set_password(self, password):
    # Creates a hashed password
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
    # Checks hashed password
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Room(db.model):
    __tablename__ = 'room'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), unique=False, nullable=False)
    capacity = db.Column(db.Integer, unique=False, nullable=False)
    available_from = db.Column(db.Time, unique=True, nullable=False) #TODO Check
    available_to = db.Column(db.Time, unique=True, nullable=False) #TODO Check

class Booking(db.model):
    __tablename__ = 'booking'
    id = db.Column(db.Integer, primary_key=True)
    start_datetime = db.Column(db.DateTime, unique=True, nullable=False)
    end_datetime = db.Column(db.DateTime, unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)


