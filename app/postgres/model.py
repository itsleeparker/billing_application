#This Model Only Consist of all the models in the application

from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from .database import Base

#This model will be open to other Instances as well in order to make relationships between tables
#Create a Table for each model 
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer , primary_key=True , index=True)
    name = Column(String(30) , nullable=False  , index=True)
    email = Column(String(50)  , nullable=False , unique=True)
    phone_no =Column(Integer , nullable=False , unique=True)
    
    def __repr__(self) -> str:
        return "UserModel(name=%s email=%s phone=%d)" % (self.name  , self.email , self.phone_no)

