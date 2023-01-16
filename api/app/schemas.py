from typing import List,Union
from pydantic import BaseModel


class TokenData(BaseModel):
    username: Union[str, None] = None

class Token(BaseModel):
    access_token: str
    token_type: str

class User_table_create(BaseModel):
    # user_id: int
    username: str
    password: str
    class Config:
        orm_mode = True

class User_table(BaseModel):
    user_id: int
    username: str
    password: str
    class Config:
        orm_mode = True


class User_calendar_create(BaseModel):
    user_id: int
    #calendar_id: int
    class Config:
        orm_mode = True


class User_calendar(BaseModel):
    user_id: int
    calendar_id: int
    class Config:
        orm_mode = True


class Calendar_create(BaseModel):
    calendar_id: int
    # event_id: int
    created_at: str
    start_date: str
    end_date: str
    description: str
    type: str
    property: str
    class Config:
        orm_mode = True

class Calendar(BaseModel):
    calendar_id: int
    event_id: int
    created_at: str
    start_date: str
    end_date: str
    description: str
    type: str
    property: str
    class Config:
        orm_mode = True

class Reminder(BaseModel):
    event_id: int
    reminder_date: str    
    class Config:
        orm_mode = True
