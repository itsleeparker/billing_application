#This Model Only Consist of all the models in the application
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from .database import Base

#This model will be open to other Instances as well in order to make relationships between tables
#Create a Table for each model 


#Classes Here 
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer , primary_key=True , index=True)
    name = Column(String(30) , nullable=False  , index=True)
    email = Column(String(50)  , nullable=False , unique=True)
    phone_no= Column(Integer , nullable=False , unique=True)
    
    def __repr__(self) -> str:
        return "UserModel(name=%s email=%s phone=%d)" % (self.name  , self.email , self.phone_no)




class Bills(Base):
    __tablename__ = "bills"
    id = Column(Integer , primary_key=True , unique=True , index=True)
    reg_no = Column(String(20) , nullable=False , unique=True)
    customer_name = Column(String(30) ,nullable=False , unique=False)
    customer_phone = Column(String(12) ,nullable=False , unique=True)
    room_no  =  Column(Integer  , nullable=False , unique=False)
    check_in_time  = Column(String(20) , nullable=False , unique=False)
    check_out_time = Column(String(20) , nullable=False , unique=False)
    check_in_date = Column(String(10)  , nullable=False , unique=False)
    check_out_date = Column(String(10) , nullable=False , unique=False)
    price_charged_by  =Column(String(10) , nullable=True , unique=False)
    price = Column(Float , unique=False , nullable=False)
    gst  = Column(Float , unique=False , nullable=True)
    total_amount = Column(Float , unique=False , nullable=False)
    user_id = Column(Integer , ForeignKey("users.id") , nullable=False ,unique=False)
    def __repr__(self) -> str:\
        return "Bills (Reg_no =  %d room_no = %s charged_by = %s)" % (self.reg_no , self.room_no , self.price_charged_by)