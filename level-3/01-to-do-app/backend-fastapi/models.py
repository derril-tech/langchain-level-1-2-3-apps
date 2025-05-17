# Import necessary SQLAlchemy types and base model setup
from sqlalchemy import Column, Integer, String, Boolean
from database import Base  # This is your declarative base from database.py

# ✅ Define the ToDo model which represents the "todos" table in the database
class ToDo(Base):
    __tablename__ = "todos"  # Name of the table in PostgreSQL

    # 🆔 Primary key column, auto-incremented by default
    id = Column(Integer, primary_key=True, index=True)

    # 📌 Name of the to-do task
    name = Column(String, nullable=False)

    # ✅ Status of the task - completed or not (defaults to False)
    completed = Column(Boolean, default=False)
