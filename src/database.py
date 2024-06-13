from sqlalchemy import create_engine, Column, Integer, String, DateTime, Date, ForeignKey, Text, BLOB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
import os 
from pathlib import Path

PATH = Path(__file__).parent 
path_db = os.path.join(PATH, 'database', 'database.db')

if not os.path.exists(path_db):
    import models
  
CONN = f"sqlite:///{path_db}"

engine = create_engine(CONN,echo=True)
Session =  sessionmaker(bind=engine)
conect = engine.connect()
session = Session()

def get_user():
    #query =  "SELECT * FROM USUARIOS"
    query = "SELECT * FROM USUARIOS  "
    result = conect.exec_driver_sql(query)
    return result
#get_user()
print(get_user())