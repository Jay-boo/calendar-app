from POO.calendar import Calendar
from fastapi import APIRouter,Request, Depends
from routes.auth import User_Pydantic, get_current_user 




router=APIRouter()

@router.get("/")
def root(request:Request):
    return {"message": "hello"}


@router.get('/me',response_model=User_Pydantic)
async def get_user(user: User_Pydantic=Depends(get_current_user)):
        return user









@router.get("/calendar")
async def get_calendar():
    return  Calendar()


@router.get("/calendar{id}")
async def get_calendar_by_id(id):
    return Calendar()


@router.post("/calendar")
async def post_calendar(calendar):
    return  Calendar()



@router.put("/calendar{id}")
async def put_calendar(id,data):
    return  Calendar()


@router.delete("/calendar{id}")
async def delete_calendar(id):
    return  Calendar()
