from fastapi import FastAPI,Depends
from helper import TodoHelper
from user_helper import UserHelper
from dependencies import get_current_user

user_helper = UserHelper()
helper=TodoHelper()
from database import Base, engine
from models import *

Base.metadata.create_all(bind=engine)

app=FastAPI();

BASE_URL="/api/todos"


@app.get(f'{BASE_URL}')
def fetch_todos(
    user_id: int = Depends(get_current_user)
):

    todos = helper.get_todos()

    return [
        {
            "id": todo.id,
            "title": todo.title,
            "description": todo.description
        }
        for todo in todos
    ]

@app.post(f'{BASE_URL}')
def add_todo(
    title: str,
    description: str,
    user_id: int = Depends(get_current_user)
):
    return helper.create_todo(title, description)

@app.put(f'{BASE_URL}/{id}')
def update(
    id: int,
    title: str,
    description: str,
    user_id: int = Depends(get_current_user)
):
    return helper.update_todo(
        id,
        title,
        description
    )

@app.delete(f'{BASE_URL}/{id}')
def delete(
    id: int,
    user_id: int = Depends(get_current_user)
):
    return helper.delete_todo(id)


@app.post("/signup")
def signup(
    username:str,
    email:str,
    password:str
):
    return user_helper.signup(
        username,
        email,
        password
    )
    
@app.post("/login")
def login(
    username:str,
    password:str
):
    return user_helper.login(
        username,
        password
    )