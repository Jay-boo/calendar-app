
CREATE DATABASE calendar_app;

-- Connect to the database
\c calendar_app;
DROP TABLE IF EXISTS User_account CASCADE;
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
    id_user SERIAL PRIMARY KEY,
    username VARCHAR(255),
    password_hash VARCHAR(255)
);

-- Create the User_calendar table
CREATE TABLE User_calendar (
    user_id INTEGER REFERENCES User_account(id_user) ,
    id_calendar SERIAL PRIMARY KEY ,
    name_calendar VARCHAR(255)
);

-- Create the Calendar table
CREATE TABLE CalendarModel (
    calendar_id INTEGER REFERENCES User_calendar(id_calendar) ,
    id_event SERIAL PRIMARY KEY ,
    title VARCHAR(255),
    created_at TIMESTAMPTZ,
    start_date TIMESTAMPTZ,
    end_date TIMESTAMPTZ,
    description VARCHAR(255),
    type VARCHAR(255),
    property VARCHAR(255)
);

-- Create the reminder table
CREATE TABLE ReminderModel (
    id_reminder SERIAL PRIMARY KEY,
    event_id INTEGER REFERENCES CalendarModel(id_event),
    reminder_date TIMESTAMP
);


ALTER SEQUENCE user_id_seq
OWNED BY User_account.id_user;

ALTER SEQUENCE event_id_seq
OWNED BY CalendarModel.id_event;

ALTER SEQUENCE calendar_id_seq
OWNED BY User_calendar.id_calendar;

ALTER SEQUENCE reminder_id_seq
OWNED BY ReminderModel.id_reminder;
