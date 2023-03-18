#Import All The required Dependecies 
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
import uvicorn
import os
from routers import users , bills
from postgres import model as models
from postgres.database import engine

#Set the app
app:FastAPI = FastAPI()

#Set The DB Connection
models.Base.metadata.create_all(bind=engine)



DIR = os.path.dirname(__file__)
ABS_PATH_STATIC = os.path.join(DIR  , "static/")
#########################SET UP ALL THE MIDDLEWARE REQUIRED FOR THE APPLICATION###########################

#Set Up Cors 
app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"],            #Change the cors Origin According to the fronend  
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"]
)


# ##################################SET UP THE STATIC ROUTING FOR THE APPLICATION############################
app.mount("/home" , app=StaticFiles(directory=ABS_PATH_STATIC , html=True) , name="static")

# @app.exception_handler(Exception)
# def apiException(request , err):
#     err_message = f"Failed to execute {request.method} on {request.url}"
#     return JSONResponse(content={"message" : err_message , "Details" : f"{err}"}  , status_code=400)
    
# ######################## Set Up all the dedicated root routes to the application ################################
# #Home Router here 
app.include_router(bills.router)
app.include_router(users.router)


#ADD basic Routing 
@app.get("/")
async def root():
    return{
        "message" : "Welcome To billing Application Backend please go to home page to proceed" ,
        "status" : 200
    }

@app.get("/healthcheck")
async def healthcheck():
    return{
        "message" : "Server Up and Running" , 
        "status" : 200
    }

############################################# Start the applicatio ###########################################
if __name__ == "__main__":
    uvicorn.run(app , host="0.0.0.0" , port=8000)