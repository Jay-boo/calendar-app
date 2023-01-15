from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel
from typing import Optional,List
from sqlalchemy import create_engine, select
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from app import schemas,model


app = FastAPI()

username="postgres"
#os.getenv("POSTGRES_USER")
password="azerty"
#os.getenv("POSTGRES_PASSWORD")




DATABASE_URL = create_engine("postgresql://"+username+":"+password+"@localhost:5432/calendar_app",echo=True)
Base=declarative_base()


db=sessionmaker(bind=DATABASE_URL)
session = db()
session._model_changes = {}

@app.get('/')
def index():
    return {'message':'hello worldd'}

##User##
#get all users
@app.get('/user',response_model=List[schemas.User_table],status_code=200)
def get_all_items():
    items=session.query(model.User_table).all()
    return items

@app.post("/user/", response_model=schemas.User_table,status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.User_table):
    test_user =session.query(model.User_table).filter(model.User_table.username==user.username).first()

    if test_user is not None:
        raise HTTPException(status_code=400,detail="User already exists")


    db_user = model.User_table(username=user.username, password=user.password)
    session.add(db_user)
    session.commit()
    return db_user

@app.get("/user/{username}", response_model=schemas.User_table)
def read_user(username: str):
    db_user = session.query(model.User_table).filter(model.User_table.username == username).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user