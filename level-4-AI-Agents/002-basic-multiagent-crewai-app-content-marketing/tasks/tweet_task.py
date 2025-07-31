# tasks/tweet_task.py

"""
====================================================
🐦 Tweet Task for Social Media Manager Agent
====================================================

This task asks the Social Media Manager to distill the
blog article into a compelling tweet.

It uses the blog task as context and produces a
short, shareable summary (max 280 characters).
"""

# ========================
# 📦 1. Path Setup for Module Imports
# ========================

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# ========================
# 🧩 2. Import the Agent and Task
# ========================

from crewai import Task
from agents.social_media_manager import social_media_manager
from tasks.blog_task import blog_task  # 👈 Contextual input from blog

# 🐦 Define the social media task
tweet_task = Task(
    description=(
        "Based on the blog article about '{topic}', write a high-engagement tweet.\n"
        "- Max 280 characters.\n"
        "- Use emojis and hashtags if appropriate.\n"
        "- Hook the reader, but stay true to the blog’s message.\n"
        "- The tweet should invite curiosity or provide a powerful one-liner summary."
    ),
    expected_output="A concise tweet that summarizes and promotes the blog article on '{topic}'.",
    agent=social_media_manager,
    context=[blog_task]  # ✅ Uses the blog post as input
)
