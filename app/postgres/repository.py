
from typing import Any, List
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
        res  = db.query(model.User).all()
        print(res)
        return res
    
    async def deleteUser(db:Session , id:int)->Any:
        user = db.query(model.User).filter(model.User.id == id).first()
        db.delete(user)
        db.commit()
        return user
            
    async def update(db:Session , user:schema.UserCreate):
        user = db.merge(user)
        db.commit()
        return user
    
class BillsRepo():
    async def create(db:Session , bill:schema.BillsCreate):
        bill = model.Bills(
            reg_no = bill.reg_no ,
            customer_name = bill.customer_name ,
            customer_phone = bill.customer_phone,
            check_in_time  = bill.check_in_time , 
            check_out_time = bill.check_out_time  ,
            check_in_date = bill.check_in_date , 
            check_out_date = bill.check_out_date , 
            price = bill.price , 
            gst =  bill.gst ,
            user_id = bill.user_id,
            price_charged_by = bill.price_charged_by ,
            total_amount = bill.total_amount
        )
        db.add(bill)
        db.commit()
        db.refresh()
        return bill
    
    async def get_bill_by_user_id(db:Session  , user_id:int):
        res:List = db.query(model.Bills).filter(model.Bills.user_id == user_id)
        return res

    async  def get_bill_by_customer_phone(db:Session , phone:str):
        res:List = db.query(model.Bills).filter(model.Bills.customer_phone == phone)
        return res
    async def get_bill_by_id(db:Session , id:int):
        return db.query(model.Bills).filter(model.Bills.id == id).first()
    
    async def get_bills_by_date(db:Session , date:str):
        return db.query(model.Bills).filter(model.Bills.check_in_date == date)

    async def deleteBill(db:Session , id:int)->Any:
        bill = db.query(model.Bills).filter(model.Bills.id == id).first()
        db.delete(bill)
        db.commit()
        return bill 
    
    async def update(db:Session , item)->Any:
        bill = db.merge(item)
        db.commit()
        return bill