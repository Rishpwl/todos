from fastapi import FastAPI
from helper import TodoHelper
helper=TodoHelper()

app=FastAPI();

BASE_URL="/api/todos"


@app.get(f'{BASE_URL}')
def fetch_todos():
    return helper.get_todos()

@app.post(f'{BASE_URL}')
def add_todo(title:str,description:str):
    return helper.create_todo(title,description)

@app.put(f'{BASE_URL}/{id}')
def update(id:int,title:str,description:str):
    return helper.update_todo(id,title,description)

@app.delete(f'{BASE_URL}/{id}')
def delete(id:int):
    return helper.delete_todo(id)