from database import db_connection

class TodoHelper:
    def __init__(self):
        self.db=db_connection()
        self.curr=self.db.cursor()
        
    def get_todos(self):
      
      self.curr.execute("Select * from todos")
      data=self.curr.fetchall()
      self.curr.close()
      
      
      return data

    def create_todo(self,title,description):
      
      self.curr.execute(
      """
      INSERT INTO todos(title,description)
      VALUES(%s,%s)
      """,
      (title,description)
      )
      self.db.commit()
      self.curr.close()
    
    
      return {"message":"Todo created"}

    def update_todo(self,id,title,description):
    
       
    
       self.curr.execute(
        """
        UPDATE todos
        SET title=%s,description=%s
        WHERE id=%s
        """,
        (title,description,id)
        )
       self.db.commit()
       self.curr.close()
     
       return  {"message":"Todo updated"}

    def delete_todo(self,id):
   
      
      self.curr.execute(
      """
      DELETE FROM todos 
      WHERE id=%s
      """,
      (id,)
      )
    
      self.db.commit();
      self.curr.close()
    
    
      return {"message":"Todo deleted"};
      