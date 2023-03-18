
from typing import Any , List
from sqlalchemy.orm import Session
from . import model , schema

class UserRepo():
    async def createUser(db:Session , user:schema.UserCreate):
        print("This was called")
        db_user = model.User(
            name=user.name,
            email=user.email  , 
            phone_no = user.phone_no
        )
        db.add(instance=db_user)
        db.commit()
        db.refresh(instance=db_user)
        print(db_user)
        return db_user
    
    async def fetch_by_id(db:Session , _id:str)->Any:
        return db.query(model.User).filter(model.User.id == _id).first()
    
    async def fetch_by_phone(db:Session , phone_number:int)->Any:
        return db.query(model.User).filter(model.User.phone_no == phone_number).first()
    
    async def fetchAll(db:Session , skip:int , limit:int)->Any:
        return db.query(model.User).offset(skip).limit(limit=limit).all()
            
    