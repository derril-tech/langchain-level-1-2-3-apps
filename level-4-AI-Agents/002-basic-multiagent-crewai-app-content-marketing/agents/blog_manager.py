# agents/blog_manager.py

"""
====================================================
✍️ Blog Manager Agent (CrewAI - GPT-4o)
====================================================

This agent is responsible for transforming the research into
a polished, well-structured blog article.

They improve clarity, flow, and SEO while staying aligned
with the original research and tone.

This agent logs their thinking and does not delegate tasks.
"""

from crewai import Agent

# 🧠 Define the Blog Manager Agent
blog_manager = Agent(
    role="Blog Manager",
    goal="Convert the research on {topic} into a structured, engaging blog post.",
    backstory=(
        "As a professional blog manager, you transform research data into clear, well-written blog content. "
        "You polish grammar, organize ideas with proper headers, and optimize content for readability and SEO. "
        "Your writing is audience-friendly, informative, and aligned with modern blogging best practices. "
        "The final output should be something ready to publish on a reputable blog."
    ),
    verbose=True,
    allow_delegation=False
)
