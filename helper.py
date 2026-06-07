from database import db_connection

class TodoHelper:
    def __init__(self):
        self.db=db_connection()
        
    def get_todos(self):
      curr=self.db.cursor()
      curr.execute("Select * from todos")
      data=curr.fetchall()
      curr.close()
      
      
      return data

def create_todo(self,title,description):
    
    curr=self.db.cursor()
    
    curr.execute(
    """
    INSERT INTO todos(title,description)
    VALUES(%s,%s)
    """,
    (title,description)
    )
    self.db.commit()
    curr.close()
    
    
    return {"message":"Todo created"}

def update_todo(self,id,title,description):
    
    curr=self.db.cursor()
    
    curr.execute(
    """
    UPDATE todos
    SET title=%s,description=%s
    WHERE id=%s
    """,
    (title,description,id)
    )
    self.db.commit()
    curr.close()
    
    return  {"message":"Todo updated"}

def delete_todo(self,id):
   
    curr=self.db.cursor();
    curr.execute(
    """
    DELETE FROM todos 
    WHERE id=%s
    """,
    (id,)
    )
    
    self.db.commit();
    curr.close()
    
    
    return {"message":"Todo deleted"};
      