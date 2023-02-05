
import asyncio
from calendar import calendar
from datetime import datetime
from fastapi import APIRouter,Request, Depends,HTTPException
from pydantic import BaseModel
from POO.event import Event
from POO.calendar import Calendar
from POO.eventLeasure import EventLeasure
from tortoise.contrib.pydantic.creator import pydantic_model_creator
from POO.calendar import Calendar
from POO.eventLeasure import EventLeasure
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
async def create_calendar(user:User_Pydantic=Depends(get_current_user)):
    user = await User_account.get(id_user=user.id_user)
    user_calendar_obj=await User_calendar.create(user=user)
    return user_calendar_obj

# Get all calendar
@router.get("/calendar")
async def  get_user_calendars(user:User_Pydantic=Depends(get_current_user)):
    calendars=await User_calendar.filter(user=user.id_user)
    if not calendars:
        return []

        # raise HTTPException(status_code=404, detail=f"{user.username} doesn't have calendars")
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

   












Event_Pydantic=pydantic_model_creator(CalendarModel,name='EventIn',exclude_readonly=True)
class EventCreate_Pydantic(BaseModel):
        title:str 
        description:str
        start_date: datetime
        end_date:datetime
        property:str
        type:str


# -------------------------------CONFLIT--------------------------
# Necessité : En entrée il faut pas que je doivent mettre un event_id
#---------------------------------------------------------------------


# @router.post("/calendar/{calendar_id}/add_event")
# async def add_event_to_calendar(calendar_id:int,event:EventCreate_Pydantic,user:User_Pydantic=Depends(get_current_user)):
#     print(event.title)
#     print(event.start_date)
#     print(event.end_date)
#     calendar=await get_calendar(calendar_id,user)
#     if calendar!={"error":f"{user.username} doesn't have {calendar_id} calendar"}:
#         print("-------------OK")
#         events=[  EventLeasure(title=evet.title,desc=evet.description,start_time=evet.start_date.replace(tzinfo=None),end_time=evet.end_date.replace(tzinfo=None),activity="React")for evet in calendar]
#         new_event=EventLeasure(title=event.title,desc=event.description,start_time=event.start_date.replace(tzinfo=None),end_time=event.end_date.replace(tzinfo=None),activity="React")
#         calendar_POO=Calendar()
#         calendar_POO.load_calendar(events)
#         print(calendar_POO)
#         print("--------load_success")
#         print(new_event)
#         calendar_POO.add_event(new_event)
#         print("--------ok")
#         calendar_orm= await CalendarModel.create(
#                 calendar_id=calendar_id,
#                 title=new_event.title,
#                 description=new_event.desc,
#                 created_at=new_event.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
#                 start_date=new_event.start_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
#                 end_date=new_event.end_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
#                 type=event.type,
#                 property=new_event.property
#
#                 )
#         print(new_event);
#         # return {"id": calendar_orm.event_id,"start_time":new_event.start_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ"), "end_time":new_event.end_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ")}
#         return {"id": calendar_orm.event_id,"start_time":new_event.start_time, "end_time":new_event.end_time}
#     else:
#         return {"error"}




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
    
            
    events_obj =[]
    for evn in events : 
        events_obj.append(transfrom_with_strat(Event(
                    title=evn.title,
                    desc=evn.description,
                    start_time=evn.start_date,
                    end_time=evn.end_date,
                    id=evn.id_event
                    ),evn.type,evn.property))
                
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
                                   property=evn.property) if evn.id is not None 
            else CalendarModel.create(calendar_id=calendar_id,
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
            end_time=event.end_date,
            id=event_id
            ),event.type,event.property)
    if not event:
        raise HTTPException(status_code=404, detail="Type not valid")
    
            
    events_obj =[]
    for evn in events : 
        events_obj.append(transfrom_with_strat(Event(
                    title=evn.title,
                    desc=evn.description,
                    start_time=evn.start_date,
                    end_time=evn.end_date,
                    id=evn.id_event
                    ),evn.type,evn.property))
                
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

