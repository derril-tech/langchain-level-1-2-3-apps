from functools import lru_cache
from typing import Union

from fastapi import FastAPI, Depends
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.middleware.cors import CORSMiddleware

from routers import pdfs  # Enable your PDF router
import config

app = FastAPI()

# Include your routers
app.include_router(pdfs.router)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global exception handler
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    print(f"{repr(exc)}")
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

# Dependency-injected settings
@lru_cache()
def get_settings():
    return config.Settings()

# Root route using settings
@app.get("/")
def read_root(settings: config.Settings = Depends(get_settings)):
    print(settings.APP_NAME)
    return {"message": "Hello PDF World!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
