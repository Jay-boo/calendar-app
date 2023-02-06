
import asyncio
from calendar import calendar
from datetime import datetime
from fastapi import APIRouter,Request, Depends,HTTPException
from POO.event import Event
from POO.calendar import Calendar
from POO.eventLeasure import EventLeasure
from tortoise.contrib.pydantic.creator import pydantic_model_creator
from models.user import User_account
from models.calendarModel import CalendarModel, User_calendar
from routes.auth import User_Pydantic, get_current_user 
from POO.function import transfrom_with_strat

import pytz

utc=pytz.UTC



router=APIRouter()
Calendar_Pydantic=pydantic_model_creator(User_calendar,name="UserToCalendar")

#Create one calendar
@router.post("/calendar",response_model = Calendar_Pydantic)
async def create_calendar(name_calendar:str,user:User_Pydantic=Depends(get_current_user)):
    user = await User_account.get(id_user=user.id_user)

    user_calendar_obj=await User_calendar.create(user=user,name_calendar=name_calendar)
    return user_calendar_obj

# Get all calendar
@router.get("/calendar")
async def  get_all_calendar(user:User_Pydantic=Depends(get_current_user)):
    calendars=await User_calendar.filter(user=user.id_user)
    if not calendars:
        raise HTTPException(status_code=404, detail=f"{user.username} doesn't have calendars")
    return calendars

# Get calendar by id
@router.get("/calendar/{calendar_id}") # Devra retourner un calendar model
async def get_calendar(calendar_id:int,user:User_Pydantic=Depends(get_current_user)):
    calendar=await User_calendar.filter(user_id=user.id_user  , id_calendar=calendar_id)

    if not calendar:
        raise HTTPException(status_code=404, detail=f"{user.username} doesn't have {calendar_id} calendar")
    
    #else : We 're gonna look for events
    events=await CalendarModel.filter(calendar_id=calendar_id)
    if not events:
        return {}
    else:
        return events

# Delete calendar by id
@router.delete("/calendar/{calendar_id}") # Devra retourner un calendar model
async def delete_calendar(calendar_id:int,user:User_Pydantic=Depends(get_current_user)):
    calendar=await User_calendar.filter(user_id=user.id_user  , id_calendar=calendar_id)

    if not calendar:
        raise HTTPException(status_code=404, detail=f"{user.username} doesn't have {calendar_id} calendar")
    events=await CalendarModel.filter(calendar_id=calendar_id).delete()
    calendar=await User_calendar.filter(user_id=user.id_user  , id_calendar=calendar_id).delete()

   







Event_Pydantic=pydantic_model_creator(CalendarModel,name='EventIn',exclude_readonly=True)
# @router.post("/calendar/{calendar_id}/title={title}&start_time={start_time}&end_time={end_time}&type={type}")
@router.post("/calendar/{calendar_id}/event")
async def add_event_to_calendar(calendar_id:int,event:Event_Pydantic,user:User_Pydantic=Depends(get_current_user)):
    user = await User_account.get(id_user=user.id_user)
    try:
        user_calendar = await User_calendar.get(id_calendar=calendar_id,user_id=user.id_user)
    except:
        user_calendar = None
    if not user_calendar:
        raise HTTPException(status_code=404, detail=f"{user.username} doesn't have {calendar_id} calendar")

    events = await CalendarModel.filter(calendar_id=calendar_id)

    calendar_obj = Calendar()

    event=transfrom_with_strat(Event(
            title=event.title,
            desc=event.description,
            start_time=event.start_date,
            end_time=event.end_date,
            ),event.type,event.property)
    
    if not event:
        raise HTTPException(status_code=404, detail="Type not valid")
    event.id=None
    
            
    events_obj =[]
    for evn in events : 
        event_save = transfrom_with_strat(Event(
                    title=evn.title,
                    desc=evn.description,
                    start_time=evn.start_date,
                    end_time=evn.end_date
                    ),evn.type,evn.property)
        event_save.created_at = evn.created_at
        event_save.id=evn.id_event
        events_obj.append(event_save)
    
    
    calendar_obj.events=events_obj
    calendar_obj.add_event(event)

    print(calendar_obj)

    deleted_job = await CalendarModel.filter(calendar_id=calendar_id).delete()
    tasks = [CalendarModel.create(calendar_id=calendar_id,
                                   id_event = evn.id,
                                   title=evn.title,
                                   created_at=evn.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                                   start_date=evn.start_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                                   end_date=evn.end_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                                   description=evn.desc,
                                   type=evn.type,
                                   property=evn.property) if evn.id is not None 
            else CalendarModel.create(calendar_id=calendar_id,
                                   title=evn.title,
                                   created_at=datetime.now().replace(tzinfo=pytz.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                                   start_date=evn.start_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                                   end_date=evn.end_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                                   description=evn.desc,
                                   type=evn.type,
                                   property=evn.property) 
            for evn in calendar_obj.events]
    
    await asyncio.gather(*tasks)

    events = await CalendarModel.filter(calendar_id=calendar_id)
    return events
    

# Delete event by id
@router.delete("/calendar/{calendar_id}/event/{event_id}") # Devra retourner un calendar model
async def delete_event(calendar_id:int,event_id:int,user:User_Pydantic=Depends(get_current_user)):
    calendar=await User_calendar.filter(user_id=user.id_user  , id_calendar=calendar_id)

    if not calendar:
        raise HTTPException(status_code=404, detail=f"{user.username} doesn't have {calendar_id} calendar")
    events=await CalendarModel.filter(calendar_id=calendar_id,id_event=event_id)
    if not events:
        raise HTTPException(status_code=404, detail=f"{calendar_id} doesn't have {event_id} event")

    deleted_job = await CalendarModel.filter(calendar_id=calendar_id,id_event=event_id).delete()

    events = await CalendarModel.filter(calendar_id=calendar_id)
    return events

    
@router.put("/calendar/{calendar_id}/event/{event_id}")
async def update_event_to_calendar(calendar_id:int,event_id:int,event:Event_Pydantic,user:User_Pydantic=Depends(get_current_user)):
    user = await User_account.get(id_user=user.id_user)
    try:
        user_calendar = await User_calendar.get(id_calendar=calendar_id,user_id=user.id_user)
    except:
        user_calendar = None
    if not user_calendar:
        raise HTTPException(status_code=404, detail=f"{user.username} doesn't have {calendar_id} calendar")

    try :
        calendar_event = await CalendarModel.get(calendar_id=calendar_id,id_event=event_id)
    except:
        calendar_event =None
    if not calendar_event : 
        raise HTTPException(status_code=404, detail=f"Calendar {calendar_id} doesn't have {event_id} event")


    deleted_job = await CalendarModel.filter(calendar_id=calendar_id,id_event=event_id).delete()
    events = await CalendarModel.filter(calendar_id=calendar_id)

    calendar_obj = Calendar()

    event=transfrom_with_strat(Event(
            title=event.title,
            desc=event.description,
            start_time=event.start_date,
            end_time=event.end_date
            ),event.type,event.property)
    
    if not event:
        raise HTTPException(status_code=404, detail="Type not valid")
    event.id=event_id
    event.created_at = datetime.now().replace(tzinfo=pytz.utc)
    
            
    events_obj =[]
    for evn in events : 
        event_save = transfrom_with_strat(Event(
                    title=evn.title,
                    desc=evn.description,
                    start_time=evn.start_date,
                    end_time=evn.end_date
                    ),evn.type,evn.property)
        event_save.created_at = evn.created_at
        event_save.id=evn.id_event
        events_obj.append(event_save)
                
    calendar_obj.events=events_obj
    calendar_obj.add_event(event)

    deleted_job = await CalendarModel.filter(calendar_id=calendar_id).delete()
    tasks = [CalendarModel.create(calendar_id=calendar_id,
                                id_event = evn.id,
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


