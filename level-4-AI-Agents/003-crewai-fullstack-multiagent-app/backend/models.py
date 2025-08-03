# === IMPORTS ===

from typing import List
from pydantic import BaseModel


# === NAMED URL STRUCTURE ===

class NamedUrl(BaseModel):
    """
    Represents a single named URL — used for YouTube video titles + links.
    Example:
        {
            "name": "What is Generative AI?",
            "url": "https://youtube.com/..."
        }
    """
    name: str
    url: str


# === BUSINESS AREA RESULT STRUCTURE ===

class BusinessareaInfo(BaseModel):
    """
    Represents all blog and video results for a single (technology, business area) pair.
    Example:
        {
            "technology": "Generative AI",
            "businessarea": "Marketing",
            "blog_articles_urls": [...],
            "youtube_videos_urls": [...]
        }
    """
    technology: str
    businessarea: str
    blog_articles_urls: List[str]         # Simple list of blog post links
    youtube_videos_urls: List[NamedUrl]   # List of video title + link pairs


# === WRAPPER FOR LIST OF BUSINESS AREA RESULTS ===

class BusinessareaInfoList(BaseModel):
    """
    Wraps multiple BusinessareaInfo objects into a single structure.
    This is what we send to the frontend after all research is complete.
    """
    businessareas: List[BusinessareaInfo]


"""
🧠 BEGINNER NOTES — How models.py Works (CrewAI Output Schema)

🔹 1. Purpose
This file defines **data models** that structure the output of your AI agents.
These are used to validate and organize the content returned to the frontend (React/Next.js).

🔹 2. NamedUrl
This model is used for YouTube search results.
Each video result has a `name` (title) and `url` (link).
We keep them paired using this model.

🔹 3. BusinessareaInfo
This is the main result structure for a single technology + business area pair.
It includes:
- `technology` (e.g., "ChatGPT")
- `businessarea` (e.g., "Customer Service")
- A list of blog URLs (`blog_articles_urls`)
- A list of YouTube videos (`youtube_videos_urls`), each a `NamedUrl` object.

🔹 4. BusinessareaInfoList
This wraps multiple `BusinessareaInfo` objects into a single list.
This is the final return format used by the backend to respond to the frontend.

🔹 5. Why Use Pydantic?
- It automatically checks the data types (strings, lists, etc.).
- Ensures all required fields are present.
- Converts Python objects to clean, structured JSON with `.json()` or `.dict()`.

"""
