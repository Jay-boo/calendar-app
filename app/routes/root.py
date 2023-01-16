from typing import List
from POO.calendar import Calendar
from fastapi import APIRouter,Request, Depends
from models.user import User_account
from routes.auth import User_Pydantic, get_current_user 




router=APIRouter()

@router.get("/")
def root(request:Request):
    return {"message": "hello"}


@router.get('/me',response_model=User_Pydantic)
async def get_user(user: User_Pydantic=Depends(get_current_user)):
        return user



