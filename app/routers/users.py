from fastapi import APIRouter ,HTTPException , Depends
from postgres.database import getDb
from postgres import schema
from sqlalchemy.orm import Session
from postgres.repository import UserRepo
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



@router.get("/")
async def getHomePage():
    try:
        return{
            "message" : "This is User Api end point" ,
            "status" : 200
        }
    except:
        raise HTTPException(status_code=404 , detail="Page Not Found") 

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
async def get_by_phone(req:int     , db:Session = Depends(getDb)):
    try:
        return await UserRepo.fetch_by_phone(db=db , phone_number=req)
    except:
        raise HTTPException(status_code=404,  detail="Error Occured while fetching")