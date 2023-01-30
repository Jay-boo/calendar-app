from dotenv import load_dotenv
import uvicorn
from fastapi import FastAPI
from POO.calendar import Calendar
from routes import root, auth ,calendar_router
from fastapi import FastAPI,  HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from tortoise.contrib.fastapi import register_tortoise
from tortoise.contrib.pydantic import pydantic_model_creator
from dotenv import load_dotenv
import os 

load_dotenv()

# Load the calendar
# calendar=load_calendar(db,0)
calendar=Calendar(
        )
app = FastAPI()
POSTGRES_HOST=os.getenv("POSTGRES_HOST")
POSTGRES_DB=os.getenv("POSTGRES_DB")
POSTGRES_USER=os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD=os.getenv("POSTGRES_PASSWORD")
POSTGRES_PORT=os.getenv("POSTGRES_PORT")




register_tortoise(
    app, 
    db_url=f"postgres://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}",
    modules={'models': ['models.user','models.calendarModel']},
    generate_schemas=True,
    add_exception_handlers=True
)

app.include_router(root.router)
app.include_router(auth.router)
app.include_router(calendar_router.router)



if __name__=="__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")
