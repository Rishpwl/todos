from database import SessionLocal
from models import Todo

class TodoHelper:
    def __init__(self):
        self.db=SessionLocal()
        
        
    def get_todos(self):

       todos = self.db.query(Todo).all()

       return todos

    def create_todo(self, title, description):

       todo = Todo(
        title=title,
        description=description
      )

       self.db.add(todo)
       self.db.commit()
       self.db.refresh(todo)

       return {"message": "Todo created"}
    
    def update_todo(self, id, title, description):

       todo = self.db.query(Todo).filter(
          Todo.id == id
        ).first()

       if not todo:
           return {"message": "Todo not found"}

       todo.title = title
       todo.description = description

       self.db.commit()

       return {"message": "Todo updated"}

    def delete_todo(self, id):

      todo = self.db.query(Todo).filter(
        Todo.id == id
      ).first()

      if not todo:
        return {"message": "Todo not found"}

      self.db.delete(todo)
      self.db.commit()

      return {"message": "Todo deleted"}
      