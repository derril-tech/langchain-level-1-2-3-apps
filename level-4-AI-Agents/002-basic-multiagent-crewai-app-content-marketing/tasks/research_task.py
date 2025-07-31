# tasks/research_task.py

"""
====================================================
🔍 Research Task for Online Researcher Agent
====================================================

This task instructs the Online Researcher to gather factual,
insightful content about the given topic.

The output of this task will be passed to the blog manager
to form the basis of the blog article.
"""

from crewai import Task
from agents.online_researcher import online_researcher

# 📌 Define the research task
research_task = Task(
    description=(
        "Conduct in-depth research on the topic '{topic}'.\n"
        "- Find factual, current, and relevant information.\n"
        "- Cover multiple angles: benefits, challenges, examples.\n"
        "- Avoid repetition, and do not make up data.\n"
        "- Return a clean, professional summary ready to be shaped into a blog article."
    ),
    expected_output="A detailed, accurate summary of the topic '{topic}', suitable for use in a blog post.",
    agent=online_researcher
)
