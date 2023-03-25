# Meeting-Rooms
Meeting Room Booking Application
This application is a meeting room booking app where users can sign up, login, and book a meeting room.
Users can also view meeting rooms they have booked.

The application also has admin users with privelege access, who have access to a seperate 'admin' page. Here they can view all bookings, delete bookings, and add new meeting rooms.

## Prerequisites
1. Python 3 installed
2. Pip (or Pip3)

## Setup
1. Set up Venv (for macOS)
```
python3 -m venv .venv
source .venv/bin/activate
```
2. Install flask and packages
```
pip install -r requirements.txt
```
3. Run the app
```
export FLASK_APP=src/
flask run
```
## Demo Logins

Below are some user credentials for demo purposes and to view each available users' access.

### User

Email: user@user.com

Password: User
### Admin

Email: admin@admin.com

Password: Admin

## Test

Test can be run by executing the below command in the top level of the repository:
```
pytest test.py
```
