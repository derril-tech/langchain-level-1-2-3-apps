# crew_definition.py

"""
This file defines the full Crew using all agents and tasks.
It avoids circular imports by living outside the tasks/ and crew/ folders.
"""

from crewai import Crew, Process
from langchain_openai import ChatOpenAI

# Import agents
from agents.online_researcher import online_researcher
from agents.blog_manager import blog_manager
from agents.social_media_manager import social_media_manager

# Import tasks
from tasks.research_task import research_task
from tasks.blog_task import blog_task
from tasks.tweet_task import tweet_task

# LLM for managing the crew
manager_llm = ChatOpenAI(model="gpt-4o", temperature=0)

# ✅ The crew object
crew = Crew(
    agents=[online_researcher, blog_manager, social_media_manager],
    tasks=[research_task, blog_task, tweet_task],
    process=Process.sequential,
    manager_llm=manager_llm,
    memory=True,
    verbose=True
)
