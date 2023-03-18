from fastapi import APIRouter

router =  APIRouter(
    prefix="/bills" ,
    tags=["Bills"]
)


@router.get("/")
def get_bills():
    print("This end point called")
    return{
        "bills" : ["BILL"]
    }