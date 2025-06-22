from functools import lru_cache
from typing import Union

from fastapi import FastAPI, Depends
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.middleware.cors import CORSMiddleware

from routers import pdfs
import config

app = FastAPI()

# === Register API Routers ===
app.include_router(pdfs.router)

origins = [
    "http://localhost:3000",       # Local dev
    "https://pdf-manager-app.vercel.app",  # Prod (optional)
]

# === CORS Configuration (dev & prod ready) ===
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace "*" with specific domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === Global Exception Handler ===
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    print(f"{repr(exc)}")
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

# === Settings Dependency ===
@lru_cache()
def get_settings():
    return config.Settings()

# === Root Endpoint ===
@app.get("/")
def read_root(settings: config.Settings = Depends(get_settings)):
    print(settings.APP_NAME)
    return {"message": "Hello PDF World!"}

# === Demo Route ===
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
