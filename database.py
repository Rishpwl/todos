import psycopg2 
from config import *


def db_connection():
    conn=psycopg2.connect(
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    return conn

conn=db_connection();
if conn:
    print("Database connected")