from tortoise.models import Model
from tortoise import fields
from passlib.hash import bcrypt



class User_calendar(Model):
    id_calendar=fields.IntField(pk=True)
    user=fields.ForeignKeyField('models.User_account')


class CalendarModel(Model):
    id_event=fields.IntField(pk=True)
    calendar=fields.ForeignKeyField('models.User_calendar')
    title=fields.CharField(60)
    created_at=fields.DatetimeField(auto_now=True)
    start_date=fields.DatetimeField()
    end_date=fields.DatetimeField()
    description=fields.CharField(60)
    type=fields.CharField(50)
    property=fields.CharField(50)
    
    


class ReminderModel(Model):
    id_reminder=fields.IntField(pk=True)
    event=fields.ForeignKeyField('models.CalendarModel')
    reminder_timedelta=fields.TimeDeltaField()



