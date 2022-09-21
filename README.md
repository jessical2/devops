# Meeting-Rooms
Meeting Room Booking Application

## Prerequisites
1. Python 3 installed

## Setup
1. Set up Venv
For macOS:
```
python3 -m venv .venv
source .venv/bin/activate
```
2. Install flask and packages
```
python -m pip install flask
pip install flask-sqlalchemy flask-login 
```
3.
```
python
from src import db, create_app
db.create_all(app=create_app())
```
4.
```
flask seed
```
5.
```
flask run
```