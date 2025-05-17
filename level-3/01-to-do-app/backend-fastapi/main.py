from functools import lru_cache
from typing import Union

from fastapi import FastAPI, Depends
from fastapi.responses import PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException

# Import our environment-based configuration
import config

# Initialize the FastAPI application
app = FastAPI()

# Setup CORS (Cross-Origin Resource Sharing)
# This allows the frontend (e.g. React or Vercel app) to communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify the frontend domain(s)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency-injected config loader using lru_cache for performance
@lru_cache()
def get_settings():
    return config.Settings()

# Basic root endpoint to verify the app is running and read settings from .env
@app.get("/")
def read_root(settings: config.Settings = Depends(get_settings)):
    print(settings.APP_NAME)  # Shows app name from .env
    return "Everything running smoothly"

# Example route with path parameters and optional query parameter
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# Global HTTP exception handler to return plain text errors
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    print(f"{repr(exc)}")  # Logs the exception
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

# Router registration: Once todos.py is created, uncomment to include the routes
from routers import todos
app.include_router(todos.router)



"""
========================================
🌐 main.py - FastAPI App Entry Point
========================================

🔹 What is FastAPI?
FastAPI is a Python web framework that helps you build APIs quickly with automatic docs, validation, and modern Python features.

🔹 What is CORS?
CORS (Cross-Origin Resource Sharing) allows your backend to accept requests from your frontend, even if they’re hosted on different domains (like localhost and Vercel).

🔹 What does @app.get("/") do?
This defines a basic route (URL endpoint) for your app. Visiting `http://localhost:8000/` will trigger this function and return "Hello World".

🔹 What is lru_cache()?
It caches the return value of the `get_settings()` function so your app doesn't reload environment variables on every request.

🔹 What is config.Settings?
It loads environment variables from your `.env` file using Pydantic's BaseSettings, allowing you to keep secrets and configs outside the code.

🔹 What is app.add_middleware(...)?
Middleware runs before/after each request. We use `CORSMiddleware` to allow our frontend to access the backend without errors.

🔹 What is @app.exception_handler(...)?
This defines a global error handler. If something goes wrong (like a 404 error), it returns a clean, plain-text response instead of a complex JSON or HTML error.

🔹 What is a router?
Routers help you organize your routes (API endpoints) into logical files like `todos.py`. For now, we comment it out until we create the `routers/todos.py` file.

🔹 What are query parameters?
In `/items/{item_id}?q=somevalue`, `item_id` is a path parameter, and `q` is an optional query parameter.

🔹 Why are comments and order important?
Keeping code well-organized and well-commented helps both beginners and professionals understand the flow quickly — it's good developer hygiene.

"""
