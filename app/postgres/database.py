from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Iloveanime1@localhost:5432/billing_application'

#Create engine for the Postgres SQL 
engine  = create_engine(
    url=SQLALCHEMY_DATABASE_URL , echo=True   
)

#Create a session instance for each DB connection
SessionLocal = sessionmaker(bind=engine  ,autocommit=False   ,autoflush=False)

#The Base for ORM models    
Base  = declarative_base()


#DB Function which will be fetched for each different session and then closed after task is completed 
def getDb():
    #For Each instance called new session will be intiated 
    db = SessionLocal()
    try:
        yield db        #Yeild will replace or update the previously created instance 
    finally:
        db.close()      #when the task is completed the session will be closed 