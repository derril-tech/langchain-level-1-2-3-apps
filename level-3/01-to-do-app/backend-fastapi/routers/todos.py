from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status

import schemas       # Pydantic models (data validation & shape)
import crud          # The database operations defined in crud.py
from database import SessionLocal  # SQLAlchemy session factory

# ✅ Create a router with a URL prefix
router = APIRouter(prefix="/todos")

# ✅ Dependency for getting DB session per request
def get_db():
    db = SessionLocal()  # Open a new DB session
    try:
        yield db         # Pass the session to the route
    finally:
        db.close()       # Always close it after use

# ✅ POST /todos — Create a new todo
@router.post("", status_code=status.HTTP_201_CREATED)
def create_todo(todo: schemas.ToDoRequest, db: Session = Depends(get_db)):
    todo = crud.create_todo(db, todo)
    return todo

# ✅ GET /todos — Get all todos or filtered by completion
@router.get("", response_model=List[schemas.ToDoResponse])
def get_todos(completed: bool = None, db: Session = Depends(get_db)):
    todos = crud.read_todos(db, completed)
    return todos

# ✅ GET /todos/{id} — Get a specific todo by ID
@router.get("/{id}")
def get_todo_by_id(id: int, db: Session = Depends(get_db)):
    todo = crud.read_todo(db, id)
    if todo is None:
        raise HTTPException(status_code=404, detail="to do not found")
    return todo

# ✅ PUT /todos/{id} — Update an existing todo
@router.put("/{id}")
def update_todo(id: int, todo: schemas.ToDoRequest, db: Session = Depends(get_db)):
    todo = crud.update_todo(db, id, todo)
    if todo is None:
        raise HTTPException(status_code=404, detail="to do not found")
    return todo

# ✅ DELETE /todos/{id} — Delete a todo by ID
@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_todo(id: int, db: Session = Depends(get_db)):
    res = crud.delete_todo(db, id)
    if res is None:
        raise HTTPException(status_code=404, detail="to do not found")


# -------------------------------------------------------------
# 🧠 NOTES: WHAT THIS FILE DOES
# -------------------------------------------------------------
# This file defines a FastAPI router that handles all `/todos` endpoints.
# It connects incoming HTTP requests to the actual CRUD database logic.
#
# 🔧 Key Concepts Used:
# - APIRouter: Lets us modularize the routes (cleaner structure)
# - Depends(get_db): Injects a database session into each route
# - schemas: Validates and serializes incoming/outgoing data
# - crud: Contains the logic for accessing and modifying the database
#
# 🔁 Route functions:
# - POST /todos       -> create_todo()
# - GET /todos        -> get_todos() [optionally filtered by completed=true/false]
# - GET /todos/{id}   -> get_todo_by_id()
# - PUT /todos/{id}   -> update_todo()
# - DELETE /todos/{id} -> delete_todo()
#
# 🧩 How it fits together:
# - User sends a request (e.g. POST /todos)
# - FastAPI validates the request using Pydantic (schemas)
# - FastAPI injects a database session (get_db)
# - CRUD function runs against the database (e.g. insert a new row)
# - The result is returned as a response
#
# 📦 This file works hand-in-hand with:
# - models.py: defines DB schema
# - crud.py: handles the actual DB transactions
# - schemas.py: validates API input/output
# - database.py: sets up DB connection/session logic
#
# ✅ This router can be plugged into `main.py` using:
#     `app.include_router(todos.router)`
