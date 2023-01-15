from dotenv import load_dotenv
import uvicorn
from fastapi import FastAPI
from POO.database import Database
from POO.calendar import Calendar
from routes import root, auth
from fastapi import FastAPI,  HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from tortoise.contrib.fastapi import register_tortoise
from tortoise.contrib.pydantic import pydantic_model_creator

load_dotenv()
db=Database()

# Load the calendar
# calendar=load_calendar(db,0)
calendar=Calendar(

        )
app = FastAPI()

register_tortoise(
    app, 
    db_url=f"postgres://postgres:a@127.0.0.1:5432/calendarapp",
    modules={'models': ['models']},
    generate_schemas=True,
    add_exception_handlers=True
)

app.include_router(root.router)
app.include_router(auth.router)



if __name__=="__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")
