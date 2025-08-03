# === IMPORTS ===

from crewai import Agent
from langchain_openai import ChatOpenAI
from crewai_tools import SerperDevTool
from tools.youtube_search_tools import YoutubeVideoSearchTool
from typing import List


# === AGENT FACTORY CLASS ===

class ResearchAgents:
    """
    A factory class that creates both the Research Agent and Research Manager.
    These agents are used by the crew to perform delegated tasks using CrewAI tools.
    """

    def __init__(self):
        # Load the LLM to be used by all agents (shared GPT-4 instance)
        self.llm = ChatOpenAI(model="gpt-4-turbo-preview")

        # Load external tools (shared)
        self.searchInternetTool = SerperDevTool()
        self.youtubeSearchTool = YoutubeVideoSearchTool()

    def research_manager(self, technologies: List[str], businessareas: List[str]) -> Agent:
        """
        Returns a Research Manager agent that oversees the entire process,
        verifies quality, and formats the output.
        """

        return Agent(
            role="Research Manager",
            goal=f"""Generate structured JSON output with:
- 3 recent blog URLs
- 3 YouTube videos (title + URL)
For each technology in each business area.

Technologies: {technologies}
Business Areas: {businessareas}

Rules:
- Do NOT make up content
- Insert "MISSING" if you can’t find results
- Ensure every tech/area pair has 3 blogs and 3 videos""",
            backstory="""You are a critical-thinking manager responsible for verifying the
quality of AI-generated research and organizing it into a clear format.""",
            llm=self.llm,
            tools=[self.searchInternetTool, self.youtubeSearchTool],
            verbose=True,
            allow_delegation=True
        )

    def research_agent(self) -> Agent:
        """
        Returns a Research Agent that performs internet and video research.
        """

        return Agent(
            role="Research Agent",
            goal="""Search Google and YouTube for content on a given technology
used in a specific business area. Return exactly 3 blog URLs and 3 YouTube videos (title + link).""",
            backstory="""You are an efficient AI assistant trained to find and return
real, accurate links from the internet and YouTube — and only the requested information.""",
            llm=self.llm,
            tools=[self.searchInternetTool, self.youtubeSearchTool],
            verbose=True
        )

"""
🧠 BEGINNER NOTES — How agents.py Works (CrewAI Agents)

🔹 1. Purpose
This file defines the two CrewAI agents:
- A **manager** who verifies and formats the final result
- A **research agent** who searches for blog and video content

🔹 2. Tools
Agents use two built-in tools:
- `SerperDevTool`: Performs Google-like web searches
- `YoutubeVideoSearchTool`: Custom wrapper to query YouTube Data API

🔹 3. Shared LLM
We load GPT-4-turbo via `ChatOpenAI` and share it across both agents.
CrewAI takes care of managing prompts and memory.

🔹 4. Factory Design
We wrap both agents in a class so we can instantiate them cleanly from other modules:
```python
agents = ResearchAgents()
manager = agents.research_manager(...)
assistant = agents.research_agent()

🔹 5. agent(...args...)
Each agent is defined by:

role: their identity

goal: the specific task they must achieve

backstory: why they exist — helps steer behavior

tools: what tools they can use

verbose=True: prints logs to console for debugging

allow_delegation=True: only the manager can reassign tasks

🔹 6. When Called
The agents are called inside crews.py, where they’re matched with tasks.
"""