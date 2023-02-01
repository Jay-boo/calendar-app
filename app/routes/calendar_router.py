
from calendar import calendar
from datetime import datetime
from fastapi import APIRouter,Request, Depends
from POO.event import Event
from tortoise.contrib.pydantic.creator import pydantic_model_creator
from models.user import User_account
from models.calendarModel import CalendarModel, User_calendar
from routes.auth import User_Pydantic, get_current_user 





router=APIRouter()
Calendar_Pydantic=pydantic_model_creator(User_calendar,name="UserToCalendar")


@router.post("/calendar")
async def create_calendar(user:User_Pydantic=Depends(get_current_user)):
    print(user.id)
    user_calendar_obj=await User_calendar.create(id_user=user.id)
    return {"message",f"calendar create for {user.username}"}





@router.get("/calendar")
async def  get_all_calendar(user:User_Pydantic=Depends(get_current_user)):
    calendars=await User_calendar.filter(user_id=user.id)
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
    print(event.title)
    event=Event(
            title=event.title,
            desc=event.description,
            start_time=event.start_date,
            end_time=event.end_date
            )









# @router.get("/calendars",response_model=calendar_Pydantic)
# async def get_calendars(user:User_Pydantic=Depends(get_current_user)):
#     return {"hello":"world"}


