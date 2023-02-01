
import asyncio
from calendar import calendar
from datetime import datetime
from fastapi import APIRouter,Request, Depends
from POO.event import Event
from POO.calendar import Calendar
from POO.eventLeasure import EventLeasure
from tortoise.contrib.pydantic.creator import pydantic_model_creator
from models.user import User_account
from models.calendarModel import CalendarModel, User_calendar
from routes.auth import User_Pydantic, get_current_user 


import pytz

utc=pytz.UTC



router=APIRouter()
Calendar_Pydantic=pydantic_model_creator(User_calendar,name="UserToCalendar")


@router.post("/calendar",response_model = Calendar_Pydantic)
async def create_calendar(user:User_Pydantic=Depends(get_current_user)):
    user = await User_account.get(id_user=user.id_user)

    user_calendar_obj=await User_calendar.create(user=user)
    return user_calendar_obj


@router.get("/calendar")
async def  get_all_calendar(user:User_Pydantic=Depends(get_current_user)):
    calendars=await User_calendar.filter(user=user.id_user)
    if not calendars:
        return {"error":"no calendar"}
    return calendars


@router.get("/calendar/{calendar_id}") # Devra retourner un calendar model
async def get_calendar(calendar_id:int,user:User_Pydantic=Depends(get_current_user)):
    calendar=await User_calendar.filter(user_id=user.id  , id_calendar=calendar_id)

    if not calendar:
        return {"error":f"{user.username} doesn't have {calendar_id} calendar"}
    
    #else : We 're gonna look for events
    events=await CalendarModel.filter(calendar_id=calendar_id)
    if not events:
        return {}
    else:
        return events







Event_Pydantic=pydantic_model_creator(CalendarModel,name='EventIn',exclude_readonly=True)
# @router.post("/calendar/{calendar_id}/title={title}&start_time={start_time}&end_time={end_time}&type={type}")
@router.post("/calendar/{calendar_id}/add_event")
async def add_event_to_calendar(calendar_id:int,event:Event_Pydantic,user:User_Pydantic=Depends(get_current_user)):
    user = await User_account.get(id_user=user.id_user)
    try:
        user_calendar = await User_calendar.get(id_calendar=calendar_id)
        if user.id_user != user_calendar.user_id:
            return {"error": "User don't have access to this calendar"}
    except User_calendar.DoesNotExist:
        return {"error": "Calendar not found"}

    events = await CalendarModel.filter(calendar_id=calendar_id)

    calendar_obj = Calendar()

    event=EventLeasure(
            title=event.title,
            desc=event.description,
            start_time=event.start_date,
            end_time=event.end_date,
            activity=event.property
            )
    
            
    events_obj =[]
    for evn in events : 
        events_obj.append(EventLeasure(
                    title=evn.title,
                    desc=evn.description,
                    start_time=evn.start_date,
                    end_time=evn.end_date,
                    activity=evn.property
                    ))
                
    calendar_obj.events=events_obj
    calendar_obj.add_event(event)

    deleted_job = await CalendarModel.filter(calendar_id=user_calendar.user_id).delete()
    tasks = [CalendarModel.create(calendar_id=calendar_id,
                                   title=evn.title,
                                   created_at=evn.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                                   start_date=evn.start_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                                   end_date=evn.end_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                                   description=evn.desc,
                                   type=evn.type,
                                   property=evn.property) 
            for evn in calendar_obj.events]
    
    await asyncio.gather(*tasks)

    events = await CalendarModel.filter(calendar_id=calendar_id)
    return events
    
















# @router.get("/calendars",response_model=calendar_Pydantic)
# async def get_calendars(user:User_Pydantic=Depends(get_current_user)):
#     return {"hello":"world"}


