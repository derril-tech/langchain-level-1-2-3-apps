# main.py

"""
==========================================================
🧠 CrewAI Multi-Agent App: Content Marketing Team (GPT-4o)
==========================================================

This app simulates a content marketing workflow using CrewAI:
- The Online Researcher gathers information
- The Blog Manager writes a full article
- The Social Media Manager crafts a tweet
- CrewAI handles sequential delegation across agents

You must have a `.env` file with your OpenAI key and other secrets.
"""

# ========================
# 📦 1. Environment Setup: Path & Variables
# ========================

import sys
import os
from dotenv import load_dotenv, find_dotenv

# 🔍 Ensure the root folder is added to the Python module path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 🔐 Load .env variables (like OPENAI_API_KEY)
_ = load_dotenv(find_dotenv())
openai_api_key = os.environ["OPENAI_API_KEY"]

# ========================
# 🚀 2. Load and Run the Crew
# ========================

from crew.crew_config import crew  # Import your crew from the crew folder

if __name__ == "__main__":
    # 👤 This is the user request to trigger the crew workflow
    input_data = {
        "topic": "the benefits of lifting heavy weights"
    }

    print("🚀 Starting the CrewAI multi-agent content flow...\n")

    # ⛳ Kickoff the crew execution
    result = crew.kickoff(inputs=input_data)

    # 🖨️ Display the final result (usually the tweet)
    print("\n✅ Final Output:\n")
    print(result)
