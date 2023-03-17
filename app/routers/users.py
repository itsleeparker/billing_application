from fastapi import APIRouter ,HTTPException

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
def getHomePage():
    try:
        return{
            "message" : "This is User Api end point" ,
            "status" : 200
        }
    except:
        raise HTTPException(status_code=404 , detail="Page Not Found") 

