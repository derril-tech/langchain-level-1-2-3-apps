# agents/online_researcher.py

"""
====================================================
🔎 Online Researcher Agent (CrewAI - GPT-4o)
====================================================

This agent is responsible for gathering up-to-date, relevant
information on a specific topic provided by the user.

The agent can be enhanced with tools like web scraping or search,
but even without tools, it performs intelligent summarization.

This agent does NOT delegate and logs everything (verbose=True).
"""

from crewai import Agent

# 🔧 Define the Online Researcher Agent
online_researcher = Agent(
    role="Online Researcher",
    goal="Collect accurate, real-time information about {topic}.",
    backstory=(
        "You are a research specialist focused on gathering high-quality data "
        "from web sources, reports, articles, and news. Your job is to understand "
        "the core of any topic quickly and provide rich insights to support the content team. "
        "You do not guess or speculate — you find real, relevant facts to build the foundation "
        "for blogs and social media posts."
    ),
    verbose=True,
    allow_delegation=False
)
