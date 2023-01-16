
from calendar import calendar
from fastapi import APIRouter,Request, Depends
from tortoise.contrib.pydantic.creator import pydantic_model_creator
from models.user import User_account
from models.calendarModel import User_calendar
from routes.auth import User_Pydantic, get_current_user 





router=APIRouter()
Calendar_Pydantic=pydantic_model_creator(User_calendar,name="UserToCalendar")


@router.post("/create_calendar")
async def create_calendar(user:User_Pydantic=Depends(get_current_user)):
    print(user.id)
    # user_calendar_obj=User_calendar(user_id=user.id)
    return {"hello","world"}

@router.get("/get_calendars")
async def  get_all_calendar(user:User_Pydantic=Depends(get_current_user)):
    calendars=await User_calendar.filter(user_id=user.id)
    if not calendars:
        return {"error":"no calendar"}
    return  {"hello": "world"}


# @router.get("/calendars",response_model=calendar_Pydantic)
# async def get_calendars(user:User_Pydantic=Depends(get_current_user)):
#     return {"hello":"world"}


