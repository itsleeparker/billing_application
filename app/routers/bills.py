from fastapi import APIRouter,Depends , HTTPException
from postgres.database import getDb
from postgres import schema, model
from postgres.repository import BillsRepo
from sqlalchemy.orm import Session
from typing import  Any
router =  APIRouter(
    prefix="/bills" ,
    tags=["Bills"]
)




@router.get("/")
def get_bills():
    """
        Basic Check Bill end point to validate the endpoint
    """
    print("This end point called")
    return{
        "bills" : ["BILL"]
    }

@router .post("/create-bill")
async def create_bill(body:schema.BillsCreate  , db:Session=Depends(getDb)):
    """
        Create a user Bill
    """
    try:
        res = await BillsRepo.create(bill=body ,db=db)
        return res
    except Exception as e:
        print(e)
        raise HTTPException(detail="Error While creating Bill",status_code=505)

@router.delete("/{id}")
async  def delete(id:int ,db:Session=Depends(getDb)):
    try:
        res = await BillsRepo.deleteBill(db=db , id=id)
        return res
    except Exception as e:
        raise HTTPException(status_code=501 , detail="Error Occured while deleting!")

@router.put("/")
async def update(body:schema.BillsCreate , db:Session=Depends(getDb)):
    try:
        res = await BillsRepo.update(db=db,item=body)
        return res
    except Exception as e:
        raise HTTPException(status_code=501 ,detail="Error Occured while updating istance")

@router.get("/{id}")
async def get_bill_by_id(id:int ,db:Session=Depends(getDb) ):
    """
        Get Bill By SQL Bill ID
    """
    try:
        res = await BillsRepo.get_bill_by_id(db=db , id=id)
        if not res:
            raise HTTPException(status_code=404 , detail="Given Bill not found !")
        return res
    except Exception as e :
        print(e)
        raise HTTPException(status_code=501 , detail="Error While fetching from server")


@router.get("/by-owner/{user_id}")
async  def get_bill_by_owner(user_id:int , db:Session=Depends(getDb)):
    """
        Get All the bills of the single user
    """
    try:
        res = await BillsRepo.get_bill_by_user_id(db=db , user_id=user_id)
        if not res:
            raise HTTPException(status_code=404 , detail="No Bill found for the user")
        return res
    except Exception as e:
        print(e)
        raise HTTPException(status_code=501, detail="Error Occured ")

@router.get("/by-customer-phone/{phn}")
async def get_bill_by_customer_phone(phn:str  , db:Session=Depends(getDb)):
    """
        Get Bills of single customer by phone number
    """
    try:
        res = await BillsRepo.get_bill_by_customer_phone(phone=phn , db=db)
        if not res:
            raise HTTPException(status_code=404 , detail="No Record Found ")
        return res
    except Exception as e:
        print(e)
        raise HTTPException(status_code=501 , detail="Something went Wrong")
