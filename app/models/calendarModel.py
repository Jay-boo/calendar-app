from tortoise.models import Model
from tortoise import fields
from passlib.hash import bcrypt



class User_calendar(Model):
    calendar_id=fields.IntField(pk=True)
    user_id=fields.ForeignKeyField('models.User_account')


class CalendarModel(Model):
    event_id=fields.IntField(pk=True)
    calendar_id=fields.ForeignKeyField('models.User_calendar')
    created_at=fields.DatetimeField(auto_now=True)
    start_date=fields.DatetimeField()
    end_date=fields.DatetimeField()
    description=fields.CharField(60)
    type=fields.CharField(50)
    property=fields.CharField(50)
    
    


class ReminderModel(Model):
    reminder_id=fields.IntField(pk=True)
    event_id=fields.ForeignKeyField('models.CalendarModel')
    reminder_timedelta=fields.TimeDeltaField()



