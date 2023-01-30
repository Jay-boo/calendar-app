


-- Create the database
-- CREATE DATABASE calendarapp;
--
-- -- Connect to the database
-- \c calendar_app;
--
--
-- -- Drop the table
--
-- DROP TABLE IF EXISTS User_table CASCADE;
-- DROP TABLE IF EXISTS Calendar CASCADE;
-- DROP TABLE IF EXISTS Reminder CASCADE;
-- DROP TABLE IF EXISTS User_calendar CASCADE;
--
-- DROP SEQUENCE IF EXISTS calendar_id ;
-- DROP SEQUENCE IF EXISTS event_id ;
-- DROP SEQUENCE IF EXISTS user_id ;
--
-- CREATE SEQUENCE calendar_id_seq;
-- CREATE SEQUENCE event_id_seq;
-- CREATE SEQUENCE user_id_seq;
--
--
--
-- -- Create the User table
-- CREATE TABLE User_table (
--     user_id INTEGER PRIMARY KEY,
--     username VARCHAR(255),
--     password VARCHAR(255)
-- );
--
-- -- Create the User_calendar table
-- CREATE TABLE User_calendar (
--     user_id INTEGER REFERENCES User_table(user_id),
--     calendar_id INTEGER PRIMARY KEY,
--     name VARCHAR(255)
-- );
--
-- -- Create the Calendar table
-- CREATE TABLE Calendar (
--     calendar_id INTEGER REFERENCES User_calendar(calendar_id) ,
--     event_id INTEGER PRIMARY KEY,
--     created_at DATE,
--     start_date DATE,
--     end_date DATE,
--     description VARCHAR(255),
--     type VARCHAR(255),
--     property VARCHAR(255)
-- );
--
-- -- Create the reminder table
-- CREATE TABLE Reminder (
--     event_id INTEGER REFERENCES Calendar(event_id),
--     reminder_date TIMESTAMP
-- );
=======
CREATE DATABASE calendar_app;

-- Connect to the database
\c calendar_app;


-- Drop the table

DROP TABLE IF EXISTS User_table CASCADE;
DROP TABLE IF EXISTS Calendar CASCADE;
DROP TABLE IF EXISTS Reminder CASCADE;
DROP TABLE IF EXISTS User_calendar CASCADE;

DROP SEQUENCE IF EXISTS calendar_id_seq ;
DROP SEQUENCE IF EXISTS event_id_seq ;
DROP SEQUENCE IF EXISTS user_id_seq ;
DROP SEQUENCE IF EXISTS reminder_id_seq ;


CREATE SEQUENCE calendar_id_seq;
CREATE SEQUENCE event_id_seq;
CREATE SEQUENCE user_id_seq;
CREATE SEQUENCE reminder_id_seq;


-- Create the User table
CREATE TABLE User_account (
    user_id INTEGER PRIMARY KEY nextval('user_id_seq'),
    username VARCHAR(255),
    password_hasg VARCHAR(255)
);

-- Create the User_calendar table
CREATE TABLE User_calendar (
    user_id INTEGER REFERENCES User_table(user_id) ,
    calendar_id INTEGER PRIMARY KEY nextval('calendar_id_seq'),
);

-- Create the Calendar table
CREATE TABLE Calendar (
    calendar_id INTEGER REFERENCES User_calendar(calendar_id) ,
    event_id INTEGER PRIMARY KEY nextval('event_id_seq'),
    title VARCHAR(255),
    created_at DATE,
    start_date DATE,
    end_date DATE,
    description VARCHAR(255),
    type VARCHAR(255),
    property VARCHAR(255)
);

-- Create the reminder table
CREATE TABLE Reminder (
    reminder_id INTEGER PRIMARY KEY nextval('reminder_id_seq'),
    event_id INTEGER REFERENCES Calendar(event_id),
    reminder_date TIMESTAMP
);


ALTER SEQUENCE user_id_seq
OWNED BY User_table.user_id;

ALTER SEQUENCE event_id_seq
OWNED BY Calendar.event_id;

ALTER SEQUENCE calendar_id_seq
OWNED BY User_calendar.calendar_id;

ALTER SEQUENCE reminder_id_seq
OWNED BY Reminder.reminder_id;
>>>>>>> cd5993a95a8ce56ab8cbfef037dcafe4aaa5ce69
