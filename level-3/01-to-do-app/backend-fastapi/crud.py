from sqlalchemy.orm import Session
import models, schemas  # models = SQLAlchemy table definitions, schemas = Pydantic validation schemas

# CREATE operation: Adds a new todo item to the database
def create_todo(db: Session, todo: schemas.ToDoRequest):
    # Create a new ToDo object from the incoming request
    db_todo = models.ToDo(name=todo.name, completed=todo.completed)
    db.add(db_todo)           # Add the new object to the current DB session
    db.commit()               # Save (commit) the new record in the database
    db.refresh(db_todo)       # Refresh to get the latest DB-generated values (like id)
    return db_todo            # Return the newly created todo item

# READ operation: Get a list of todos, optionally filtered by completion status
def read_todos(db: Session, completed: bool):
    if completed is None:
        # If no filter is applied, return all todos
        return db.query(models.ToDo).all()
    else:
        # If a filter is applied, return todos that match the completed value
        return db.query(models.ToDo).filter(models.ToDo.completed == completed).all()

# READ operation: Get a single todo by its ID
def read_todo(db: Session, id: int):
    # Query the database for the todo with the matching ID
    return db.query(models.ToDo).filter(models.ToDo.id == id).first()

# UPDATE operation: Update an existing todo item with new data
def update_todo(db: Session, id: int, todo: schemas.ToDoRequest):
    db_todo = db.query(models.ToDo).filter(models.ToDo.id == id).first()  # Get the existing todo
    if db_todo is None:
        return None  # If not found, return None
    # Update the name and completed fields of the todo
    db.query(models.ToDo).filter(models.ToDo.id == id).update({
        'name': todo.name,
        'completed': todo.completed
    })
    db.commit()         # Save the changes
    db.refresh(db_todo) # Refresh the object to reflect the update
    return db_todo      # Return the updated todo

# DELETE operation: Delete a todo item by its ID
def delete_todo(db: Session, id: int):
    db_todo = db.query(models.ToDo).filter(models.ToDo.id == id).first()  # Get the todo to delete
    if db_todo is None:
        return None  # If not found, return None
    db.query(models.ToDo).filter(models.ToDo.id == id).delete()  # Delete the record
    db.commit()  # Commit the deletion
    return True  # Return success


# -------------------------------------------------------------
# 🧠 NOTES: WHAT THIS FILE DOES
# -------------------------------------------------------------
# This file defines core CRUD (Create, Read, Update, Delete) functions
# that interact with the PostgreSQL database using SQLAlchemy ORM.
#
# Each function takes a `db` parameter (a database session) which is injected
# from FastAPI via the `Depends(get_db)` mechanism.
#
# Functions:
# - create_todo: Adds a new ToDo item using a Pydantic schema
# - read_todos: Returns all todos, or only those that are completed/incomplete
# - read_todo:  Gets a single todo by its primary key (ID)
# - update_todo: Updates name/completed status of an existing todo
# - delete_todo: Deletes a todo by its ID
#
# Files involved:
# - `models.py` defines the ToDo table structure
# - `schemas.py` defines the request/response data models
#
# These functions will be used in your FastAPI route handlers to manage todos
# when responding to HTTP requests like GET, POST, PUT, DELETE.
