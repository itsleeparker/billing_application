from fastapi import APIRouter ,HTTPException , Depends
from postgres.database import getDb
from postgres import schema
from sqlalchemy.orm import Session
from postgres.repository import  UserRepo
from typing import  Any
"""
==============================================================================
                        Home Page Router 
    All The view part of the application will be handled at this endpoint 
==============================================================================
"""
router = APIRouter(
        prefix="/user" , 
        tags=["User"],
        responses={404 : {"message" : "An Error Occured"}}
)



# @router.get("/")
# async def getHomePage():
#     try:
#         return{
#             "message" : "This is User Api end point" ,
#             "status" : 200
#         }
#     except:
#         raise HTTPException(status_code=404 , detail="Page Not Found")

@router.get("/")
async def getAllUser(db:Session= Depends(getDb)):
    """
        Get All the user in the database
    """
    try:
        user = await UserRepo.fetchAll(limit=0,skip=0 , db=db)
        if not user:
            raise HTTPException(status_code=404 , detail="No Users Found ")
        return user
    except Exception as e:
        print(e)
        raise HTTPException(status_code=505 , detail="Error Occured  , Something went wrong")
    pass

@router.get("/{id}")
async def getById(id:Any , db:Session = Depends(getDb)):
    """ 
        Get a user by the DB Id 
    """
    try:
        user = await UserRepo.fetch_by_id(db=db , _id=id)
        if not user:
            raise HTTPException(status_code=404   , detail="User Not Found ")
        return user
    except Exception as e:
        raise HTTPException(status_code=400 , detail="Something Went Wrong")

@router.post("/" , response_model=schema.User)
async def createUser(req:schema.UserCreate  , db:Session = Depends(getDb)):
    """
            Create a User and Stores the user 
    """
    existing = await UserRepo.fetch_by_phone(db=db , phone_number=req.phone_no)
    if existing:
        raise HTTPException(status_code=400  ,detail="User Already Exisit !")
    return await UserRepo.createUser(db=db , user=req)


@router.post("/get-by-phone" , response_model=schema.User)
async def get_by_phone(req:int , db:Session = Depends(getDb)):
    """
        Get A user by given Phone no 
    """
    try:
        return await UserRepo.fetch_by_phone(db=db , phone_number=req)
    except:
        raise HTTPException(status_code=404,  detail="Error Occured while fetching")

@router.put("/")
async  def update(body:schema.UserCreate , db:Session=Depends(getDb)):
    try:
        res = await UserRepo.update(user=body , db=db)
        return res
    except Exception as e:
        print(e)
        raise HTTPException(status_code=501 , detail="Something went wrong ")
