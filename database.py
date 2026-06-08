#import psycopg2 
from config import *


#def db_connection():
#   conn=psycopg2.connect(
#       database=DB_NAME,
#       user=DB_USER,
#       password=DB_PASSWORD,
#       host=DB_HOST,
#       port=DB_PORT
#   )
#   return conn

#conn=db_connection();
#if conn:
#   print("Database connected")


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:Rishabh@localhost:5432/todoapp"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
    