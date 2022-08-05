from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return "Meeting Rooms"

if __name__== "__main__":
    app.run()