from typing import List ,  Optional
from pydantic import BaseModel

#This will act as the base model to interact with ORM
class UserBase(BaseModel):
    name:str
    phone_no:int
    email:str

class UserCreate(UserBase):
    pass


#This will be the base ORM model to interact with the application directly 
class User(UserBase):
    id: int
    
    class Config:
        orm_mode = True