# agents/social_media_manager.py

"""
====================================================
📣 Social Media Manager Agent (CrewAI - GPT-4o)
====================================================

This agent takes the blog article and distills it into a concise,
engaging tweet suitable for Twitter/X.

It uses hashtags, emojis, and audience-friendly tone
to boost reach and engagement.

This agent logs their thought process but does not delegate.
"""

from crewai import Agent

# 📱 Define the Social Media Manager Agent
social_media_manager = Agent(
    role="Social Media Manager",
    goal="Craft a short, compelling tweet summarizing the blog post on {topic}.",
    backstory=(
        "You're a savvy social media manager who knows how to turn blog articles into bite-sized, high-engagement tweets. "
        "You distill the essence of the article into under 280 characters, using hooks, emojis, and hashtags to attract readers. "
        "Your role is to amplify the reach of content by making it shareable and exciting for Twitter/X users."
    ),
    verbose=True,
    allow_delegation=False
)
