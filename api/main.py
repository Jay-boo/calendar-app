from fastapi import FastAPI,status,HTTPException,Depends
from pydantic import BaseModel
from typing import Union,List
from datetime import datetime, timedelta
from sqlalchemy import create_engine, select
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from app import schemas,model
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


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

###### LOGIN #####
# source : https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def authenticate_user(username: str, password: str):
    user = read_user(username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = schemas.TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = read_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


@app.post("/token", response_model=schemas.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    tokenfin = schemas.Token(access_token=access_token,token_type="bearer")
    return tokenfin


@app.get("/me", response_model=schemas.User_table)
async def read_users_me(current_user: schemas.User_table = Depends(get_current_user)):
    return current_user

###### ##### #####


##User##
#get all users
@app.get('/user',response_model=List[schemas.User_table],status_code=200)
def get_all_items():
    items=session.query(model.User_table).all()
    return items

#register user
@app.post("/user/", response_model=schemas.User_table_create,status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.User_table_create):
    test_user =session.query(model.User_table).filter(model.User_table.username==user.username).first()

    if test_user is not None:
        raise HTTPException(status_code=400,detail="User already exists")

    db_user = model.User_table(username=user.username, password=get_password_hash(user.password))
    session.add(db_user)
    session.commit()
    return db_user

#see user by name
@app.get("/user/{username}", response_model=schemas.User_table)
def read_user(username: str):
    db_user = session.query(model.User_table).filter(model.User_table.username == username).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


##Calendar##
## Create calendar

## Add event to calendar


##get all calendar of a user
@app.get('/calendar_user/{user_id}',response_model=List[schemas.Calendar],status_code=200)
def get_all_calendar(current_user: schemas.User_table = Depends(get_current_user)):
    id=current_user.user_id
    list_calendar = session.query(model.User_calendar).filter(model.User_table.user_id==id).all()
    return list_calendar