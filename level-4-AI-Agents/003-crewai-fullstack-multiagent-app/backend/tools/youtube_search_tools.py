# === IMPORTS ===

from typing import List, Type
from pydantic.v1 import BaseModel, Field
import os
import requests
from crewai_tools import BaseTool


# === INPUT + OUTPUT MODELS ===

class VideoSearchResult(BaseModel):
    """
    Represents a single YouTube video result (title + link).
    """
    title: str
    video_url: str


class YoutubeVideoSearchToolInput(BaseModel):
    """
    Input schema for the YouTube search tool.
    """
    keyword: str = Field(..., description="The search keyword.")
    max_results: int = Field(10, description="Max number of videos to return.")


# === CUSTOM TOOL CLASS ===

class YoutubeVideoSearchTool(BaseTool):
    """
    A custom CrewAI tool that searches YouTube using the YouTube Data API v3.
    Returns a list of video results (title + URL).
    """

    name: str = "Search YouTube Videos"
    description: str = "Searches YouTube based on a keyword and returns video results."
    args_schema: Type[BaseModel] = YoutubeVideoSearchToolInput

    def _run(self, keyword: str, max_results: int = 10) -> List[VideoSearchResult]:
        """
        Executes the YouTube API call and parses the results.
        """

        # Read API key from environment
        api_key = os.getenv("YOUTUBE_API_KEY")

        # Construct request
        url = "https://www.googleapis.com/youtube/v3/search"
        params = {
            "part": "snippet",
            "q": keyword,
            "maxResults": max_results,
            "type": "video",
            "key": api_key
        }

        # Make request
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise exception if not 200

        items = response.json().get("items", [])
        results = []

        # Parse each item in response
        for item in items:
            title = item["snippet"]["title"]
            video_id = item["id"]["videoId"]
            video_url = f"https://www.youtube.com/watch?v={video_id}"

            results.append(VideoSearchResult(
                title=title,
                video_url=video_url
            ))

        return results


"""
🧠 BEGINNER NOTES — How youtube_search_tools.py Works (CrewAI Custom Tool)

🔹 1. Purpose
This file defines a custom CrewAI tool that lets agents search YouTube and return real videos
based on a user keyword. It's attached to the Research Agent.

🔹 2. Models
We use Pydantic to define:
- `YoutubeVideoSearchToolInput`: What the agent must provide (a keyword, max results).
- `VideoSearchResult`: What the tool returns (video title + link).

🔹 3. _run() Method
Every CrewAI tool must define a `_run()` function.
This:
- Takes a keyword (e.g. "Generative AI in marketing")
- Makes an HTTP GET request to YouTube's API
- Extracts the video titles and IDs
- Returns a list of results

🔹 4. YOUTUBE_API_KEY
The YouTube API key is loaded from the environment.
Make sure to define it in your `.env` file inside `backend/` like this:

    YOUTUBE_API_KEY=your_api_key_here

You can get a key at https://console.cloud.google.com/ by enabling the "YouTube Data API v3".

🔹 5. Return Value
This tool returns a list of structured video objects that your agents can use directly
or include in their output.

🔹 6. Why a Custom Tool?
CrewAI lets you define your own tools using any external API.
This one wraps the official YouTube API and formats the results nicely
so the LLM doesn’t have to interpret raw JSON.

"""
