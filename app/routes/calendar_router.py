
from pydantic import BaseModel
from asyncio import events
from calendar import calendar
from datetime import datetime,date
from fastapi import APIRouter,Request, Depends
from POO.event import Event
from tortoise.contrib.pydantic.creator import pydantic_model_creator
from POO.calendar import Calendar
from POO.eventLeasure import EventLeasure
from models.user import User_account
from models.calendarModel import CalendarModel, User_calendar
from routes.auth import User_Pydantic, get_current_user 





router=APIRouter()
Calendar_Pydantic=pydantic_model_creator(User_calendar,name="UserToCalendar")


@router.post("/create_calendar")
async def create_calendar(user:User_Pydantic=Depends(get_current_user)):
    user_calendar_obj=await User_calendar.create(user_id=user.user_id)
    return {"calendar_id":user_calendar_obj.calendar_id}





@router.get("/get_calendars")
async def  get_all_calendar(user:User_Pydantic=Depends(get_current_user)):
    calendars=await User_calendar.filter(user_id=user.user_id)
    if not calendars:
        return {"error":"no calendar"}
    return calendars


@router.get("/calendar/{calendar_id}") # Devra retourner un calendar model
async def get_calendar(calendar_id:int,user:User_Pydantic=Depends(get_current_user)):
    calendar=await User_calendar.filter(user_id=user.user_id  , calendar_id=calendar_id)

    if not calendar:
        return {"error":f"{user.username} doesn't have {calendar_id} calendar"}
    
    #else : We 're gonna look for events
    events=await CalendarModel.filter(calendar_id=calendar_id)
    if not events:
        return {}
    else:
        return events







Event_Pydantic=pydantic_model_creator(CalendarModel,name='EventIn',exclude_readonly=True)
class EventCreate_Pydantic(BaseModel):
        title:str 
        description:str
        start_date: datetime
        end_date:datetime
        property:str
        type:str



@router.post("/calendar/{calendar_id}/add_event")
async def add_event_to_calendar(calendar_id:int,event:EventCreate_Pydantic,user:User_Pydantic=Depends(get_current_user)):
    print(event.title)
    print(event.start_date)
    print(event.end_date)
    calendar=await get_calendar(calendar_id,user)
    if calendar!={"error":f"{user.username} doesn't have {calendar_id} calendar"}:
        print("-------------OK")
        events=[  EventLeasure(title=evet.title,desc=evet.description,start_time=evet.start_date.replace(tzinfo=None),end_time=evet.end_date.replace(tzinfo=None),activity="React")for evet in calendar]
        new_event=EventLeasure(title=event.title,desc=event.description,start_time=event.start_date.replace(tzinfo=None),end_time=event.end_date.replace(tzinfo=None),activity="React")
        calendar_POO=Calendar()
        calendar_POO.load_calendar(events)
        print(calendar_POO)
        print("--------load_success")
        print(new_event)
        calendar_POO.add_event(new_event)
        print("--------ok")
        calendar_orm= await CalendarModel.create(
                calendar_id=calendar_id,
                title=new_event.title,
                description=new_event.desc,
                created_at=new_event.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                start_date=new_event.start_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                end_date=new_event.end_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                type=event.type,
                property=new_event.property

                )
        print(new_event);
        # return {"id": calendar_orm.event_id,"start_time":new_event.start_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ"), "end_time":new_event.end_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ")}
        return {"id": calendar_orm.event_id,"start_time":new_event.start_time, "end_time":new_event.end_time}
    else:
        return {"error"}










# @router.get("/calendars",response_model=calendar_Pydantic)
# async def get_calendars(user:User_Pydantic=Depends(get_current_user)):
#     return {"hello":"world"}


