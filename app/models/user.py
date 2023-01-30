
from tortoise.models import Model
from tortoise import fields
from passlib.hash import bcrypt

class User_account(Model):
    user_id = fields.IntField(pk=True)
    username = fields.CharField(50, unique=True)
    password_hash = fields.CharField(128)


    @classmethod
    async def get_user(cls,username):
        return cls.get(username=username)
    

    def verify_password(self,password):
        return bcrypt.verify(password,self.password_hash)
