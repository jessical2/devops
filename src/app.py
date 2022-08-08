from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
db = SQLAlchemy(app)

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


