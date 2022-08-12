DROP TABLE IF EXISTS user;

CREATE TABLE user (
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);

CREATE TABLE room (
    room_id INTEGER PRIMARY KEY AUTOINCREMENT,
    room_name TEXT NOT NULL,
    capacity INTEGER NOT NULL,
    available_from TEXT NOT NULL, -- ISO8601
    available_to TEXT NOT NULL
    -- telephone BOOLEAN NOT NULL CHECK (IN (0,1)),
    -- projector BOOLEAN NOT NULL CHECK (IN (0,1)),
    -- CHECK (telephone IN (0,1)),
    -- CHECK (projector IN (0,1))
)

CREATE TABLE booking (
    booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
    start_datetime TEXT NOT NULL,
    end_datetime TEXT NOT NULL,
    employee_id INTEGER NOT NULL,
    room_id INTEGER NOT NULL ,
    FOREIGN KEY (employee_id) REFERENCES user (employee_id),
    FOREIGN KEY (room_id) REFERENCES room (room_id)
)