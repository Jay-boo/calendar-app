from fastapi import APIRouter
import jwt
from fastapi import  Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.hash import bcrypt
from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator
from models.user import User_account



router=APIRouter()
JWT_SECRET="mysecret"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


#------------
# Create Schema from tortoise model
User_Pydantic =pydantic_model_creator(User_account,name='User')
UserIn_Pydantic=pydantic_model_creator(User_account,name='UserIn',exclude_readonly=True)

class UserCreate_Pydantic(BaseModel):
        username:str 
        password:str



async def authenticate_user(username:str,password:str):
        """
        Test if user is in db and if its the case then it verify its password based on hash
        """
        user=await User_account.get(username=username)
        if not user:
                return False
        if not user.verify_password(password):
                return False
        return user

async def get_current_user(token:str=Depends(oauth2_scheme)):
        try: 
                payload=jwt.decode(token,JWT_SECRET,algorithms=['HS256'])
                user=await User_account.get(id_user=payload.get('id_user'))
        except:
                raise HTTPException(
                                status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Invalid credentials"
                )
        return await User_Pydantic.from_tortoise_orm(user)


@router.post('/token')
async def generate_token(form_data: OAuth2PasswordRequestForm=Depends()):
        user=await authenticate_user(form_data.username,form_data.password)
        
        if not user:
                return {'error': 'invalid credentials'}
        user_obj = await User_Pydantic.from_tortoise_orm(user)#Convert user to a User_account  python object
        token=jwt.encode(user_obj.dict(),JWT_SECRET)
        
        return {'access_token':token,'token_type':'bearer'}


@router.post('/user',response_model=User_Pydantic)
async def create_user(user:UserCreate_Pydantic):
        user_obj=User_account(username=user.username,password_hash=bcrypt.hash(user.password))
        await user_obj.save()
        return await User_Pydantic.from_tortoise_orm(user_obj)

@router.get('/user/me',response_model=User_Pydantic)
async def get_user(user: User_Pydantic=Depends(get_current_user)):
        return user

#Change password
@router.put("/user")
async def update_user(password:str,user: User_Pydantic=Depends(get_current_user)):
        id=user.id_user
        await User_account.filter(id_user=id).update(password_hash=bcrypt.hash(password))
        return await User_Pydantic.from_queryset_single(User_account.get(id_user=id))

#delete user
@router.delete("/user")
async def delete_user(password:str,user: User_Pydantic=Depends(get_current_user)):
        await User_account.filter(id_user=id).delete()
