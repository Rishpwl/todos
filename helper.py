from database import db_connection


def get_todos():
    conn=db_connection()
    curr=conn.cursor()
    
    curr.execute("Select * from todos")
    data=curr.fetchall()
    curr.close()
    conn.close()
    
    return data

def create_todo(title,description):
    conn=db_connection()
    curr=conn.cursor()
    
    curr.execute(
    """
    INSERT INTO todos(title,description)
    VALUES(%s,%s)
    """,
    (title,description)
    )
    conn.commit()
    curr.close()
    conn.close()
    
    return {"message":"Todo created"}

def update_todo(id,title,description):
    conn=db_connection()
    curr=conn.cursor()
    
    curr.execute(
    """
    UPDATE todos
    SET title=%s,description=%s
    WHERE id=%s
    """,
    (title,description,id)
    )
    conn.commit()
    curr.close()
    conn.close()
    
    return  {"message":"Todo updated"}

def delete_todo(id):
    conn=db_connection();
    curr=conn.cursor();
    curr.execute(
    """
    DELETE FROM todos 
    WHERE id=%s
    """,
    (id,)
    )
    
    conn.commit();
    curr.close()
    conn.close();
    
    return {"message":"Todo deleted"};
      