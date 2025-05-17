from pydantic import BaseModel

# ✅ This schema is used for creating/updating a to-do item via API requests
class ToDoRequest(BaseModel):
    name: str
    completed: bool

# ✅ This schema is used for API responses when sending to-do data back to the client
class ToDoResponse(BaseModel):
    name: str
    completed: bool
    id: int  # The database-generated ID field

    # ✅ Pydantic v2: Enables compatibility with SQLAlchemy ORM models
    model_config = {
        "from_attributes": True  # Replaces orm_mode = True
    }
