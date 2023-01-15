from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User_table(Base):
    __tablename__ = 'User_table'
    __table_args__ = {'quote':False,'extend_existing':True} 
    # user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False , primary_key=True)
    password = Column(String, nullable=False)


class User_calendar(Base):
    __tablename__ = "User_calendar"
    __table_args__ = {'quote':False,'extend_existing':True} 
    calendar_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)




class Calendar(Base):
    __tablename__ = "Calendar"
    __table_args__ = {'quote':False,'extend_existing':True} 
    event_id = Column(Integer, primary_key=True, index=True)
    calendar_id = Column(Integer, nullable=False)
    created_at = Column(String, nullable=False)
    start_date = Column(String, nullable=False)
    end_date = Column(String, nullable=False)
    description = Column(String, nullable=False)
    type = Column(String, nullable=False)
    property = Column(String, nullable=False)

class Reminder(Base):
    __tablename__ = "Reminder"
    __table_args__ = {'quote':False,'extend_existing':True} 
    event_id = Column(Integer, primary_key=True, index=True)
    reminder_date = Column(String, nullable=False)
