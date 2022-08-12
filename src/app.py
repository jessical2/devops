from multiprocessing import connection
import sqlite3

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy, event
from sqlalchemy.engine import Engine

app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
db = SQLAlchemy(app)

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

@app.route("/")
def home():
    return render_template('index.html')

# @app.route("/addrec", methods = ["POST", 'GET'])
# def addrec():
#     return
    # if request.method == 'POST':


@app.route("/booked")
def booked():
    return render_template("booked.html")

if __name__== "__main__":
    app.run()


