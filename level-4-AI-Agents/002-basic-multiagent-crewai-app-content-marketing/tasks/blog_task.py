# tasks/blog_task.py

"""
====================================================
📝 Blog Writing Task for Blog Manager Agent
====================================================

This task asks the Blog Manager to turn research into
a clean, structured blog article using markdown format.

It runs *after* the research task and uses its output
as context.
"""

# ========================
# 🔧 Add root directory to sys.path for reliable imports
# ========================

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# ========================
# 📥 Import agent and dependency task
# ========================

from agents.blog_manager import blog_manager
from tasks.research_task import research_task

# 🧠 Define the blog creation task
from crewai import Task

blog_task = Task(
    description=(
        "Based on the research summary from the Online Researcher, "
        "write a high-quality blog article about '{topic}'.\n"
        "- Improve clarity and structure.\n"
        "- Add section headers, transitions, and a conclusion.\n"
        "- Ensure it's suitable for web publication and SEO-optimized.\n"
        "- Do NOT fabricate data — stick to the research provided."
    ),
    expected_output="A blog article (300–500 words) in markdown format with headers, intro, and conclusion.",
    agent=blog_manager,
    context=[research_task]  # ✅ Pulls research output into this task
)
