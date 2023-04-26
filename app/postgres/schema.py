from typing import List ,  Optional
from pydantic import BaseModel
from enum import Enum

#####################################USER SCHEMA#############################################
#This will act as the base model to interact with ORM
class UserBase(BaseModel):
    name: str
    phone_no: int
    email: str
    password: str

class UserCreate(UserBase):
    pass


#This will be the base ORM model to interact with the application directly 
class User(UserBase):
    id: int
    
    class Config:
        orm_mode = True

###############################################################################################

###################################### BILLS SCHEMA ###########################################
#Type Declaration 
class PriceType(Enum):
    HOUR:str = "HOUR" 
    DAY:str = "DAY"

class BillsBase(BaseModel):
    reg_no : str
    room_no : int
    customer_name:str
    customer_phone:str
    check_in_time : str
    check_out_time : str
    check_in_date : str
    check_out_date : str
    check_out_time : str
    user_id : int
    price_charged_by : PriceType 
    price : float
    gst: float
    total_amount : float


class BillsCreate(BillsBase):
    pass

class Bills(BillsBase):
    id:int
    class Config:
        orm_mode = True
###############################################################################################