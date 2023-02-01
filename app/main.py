from dotenv import load_dotenv
import uvicorn
from fastapi import FastAPI
from POO.database import Database
from POO.calendar import Calendar
from routes import root, auth ,calendar_router
from fastapi import FastAPI,  HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from tortoise.contrib.fastapi import register_tortoise
from tortoise.contrib.pydantic import pydantic_model_creator

load_dotenv()

# Load the calendar
# calendar=load_calendar(db,0)
app = FastAPI()

username="postgres"
#os.getenv("POSTGRES_USER")
password="azerty"
#os.getenv("POSTGRES_PASSWORD")
port="5432"
#os.getenv("POSTGRES_PORT")
host='localhost'
#os.getenv("POSTGRES_HOST")
base_name="calendar_app"
#os.getenv("POSTGRES_BASE")
register_tortoise(
    app, 
    db_url=f"postgres://"+username+":"+password+"@"+host+":"+port+"/"+base_name,
    modules={'models': ['models.user','models.calendarModel']},
    generate_schemas=True,
    add_exception_handlers=True
)

app.include_router(root.router)
app.include_router(auth.router)
app.include_router(calendar_router.router)



if __name__=="__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info",reload=True)
