from fastapi import FastAPI
from helper import get_todos,create_todo,update_todo,delete_todo

app=FastAPI();


@app.get('/todos/')
def fetch_todos():
    return get_todos()

@app.post('/todos')
def add_todo(title:str,description:str):
    return create_todo(title,description)

@app.put('/todos/{id}')
def update(id:int,title:str,description:str):
    return update_todo(id,title,description)

@app.delete('/todos/{id}')
def delete(id:int):
    return delete_todo(id)