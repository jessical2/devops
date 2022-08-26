from multiprocessing import connection
import sqlite3

from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy, event
from flask_login import LoginManager, current_user, login_required
from sqlalchemy.engine import Engine

app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.sqlite3'

db = SQLAlchemy(app)
login_manager = LoginManager()


#  Add a session.execute ('PRAGMA foreign_keys = ON;')


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dpabi_connection, connection_record):
    if type(dpabi_connection) is sqlite3.Connection:
        cursor = dpabi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()


def get_db_connection():
    connect = sqlite3.connect('database.db')
    connect.row_factory = sqlite3.Row
    return connect

@app.route("/", methods = ["POST", "GET"])
def home():
    # connect = get_db_connection
    if request.method == "POST":
        if not request.form['username'] or not request.form['password']:
            flash('Please enter all the fields', 'error')
        else:
            user = user(request.form['username'], request.form['password'])

            db.session.add(user)
            db.session.commit()
            flash('Successfully signed up')
            return redirect(url_for('booking'))
    else:
        return render_template('login.html')

@app.route("/signup", methods = ["POST", "GET"])
def signup():
    return render_template('signup.html')


@app.route("/booking")
# @login_required
def booking():
    return render_template('booking.html')


# @app.route("/addrec", methods = ["POST", 'GET'])
# def addrec():
#     return
    # if request.method == 'POST':


@app.route("/booked")
def booked():
    return render_template("booked.html")

if __name__== "__main__":
    app.run()


