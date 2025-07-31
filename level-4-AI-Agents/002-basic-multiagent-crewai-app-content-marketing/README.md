# 🧠 01 - Multi-Agent Content Marketing Team (CrewAI + GPT-4o)

This Level 4 AI Agent project uses **CrewAI** to simulate a collaborative content marketing team — powered by OpenAI’s GPT-4o. It’s a refactored version of the original LangGraph implementation but built using CrewAI’s declarative multi-agent orchestration framework.

Each CrewAI agent mirrors a real-world marketing role:

- 🔍 **Online Researcher** — gathers insights from across the web.
- ✍️ **Blog Manager** — transforms findings into structured blog content.
- 📣 **Social Media Manager** — distills the blog into a tweet.

CrewAI coordinates these roles in a sequential, memory-enabled task pipeline — showcasing real AI teamwork.

---

## 🧩 Concepts Used

- **CrewAI** — high-level framework for designing multi-agent LLM workflows.
- **Agent / Task / Crew** — building blocks of CrewAI (like functions, steps, team).
- **LangChain + GPT-4o** — the model + abstraction layer used for intelligence.
- **Process.sequential** — CrewAI process mode where each task flows linearly.
- **Memory** — short-term, long-term, and entity memory across agents.
- **Tool Support** — can add scraping/search tools for future expansion.
- **Markdown output** — the blog is returned in clean markdown format.

---

## ▶️ How to Run

1. Clone the repo and navigate into the project directory:

```bash
git clone https://github.com/derril-tech/langchain-level-1-apps.git
cd langchain-level-1-apps/level-4-AI-Agents/002-basic-multiagent-crewai-app-content-marketing

```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## 🔐 Setup Your OpenAI Key

This app requires access to OpenAI’s GPT-4o model.

1. Visit [platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)
2. Copy your API key (it starts with `sk-...`)
3. Create a `.env` file in the project root with the following contents:

```env
OPENAI_API_KEY=your_openai_key_here
TAVILY_API_KEY=your_tavily_api_key_here  # Optional: for enhanced web search
```

🛡️ Your keys remain local and secure inside the .env file and are never exposed online.

---

## ▶️ Run the App

Once setup is complete, run the app using PowerShell or your terminal of choice:

```bash
python main.py
```

```text
You’ll see the agents work together:

Online Researcher → blog-ready summary

Blog Manager → polished article with headings

Social Media Manager → tweet with emojis + hashtags

Final tweet appears at the end of the terminal.

📌 This is a backend CLI-based app. For a UI version, consider using Streamlit or a LangChain frontend.

```

---

## 🛠️ Setup Notes

This project is part of the **LangChain Level 4 AI Agents Collection** — focusing on building structured, multi-role workflows with CrewAI.

Tech stack and environment:

- **Python 3.11**
- **CrewAI ≥ 0.28.8**
- **crewai-tools ≥ 0.1.6**
- **langchain-openai ≥ 0.0.6**
- **openai ≥ 1.14.3**
- **OpenAI (GPT-4o model)**
- **GPT-4o as the LLM backbone**
- **dotenv, requests, bs4 for environment + tool support**

> 🧪 This project is designed to teach agent design, state modeling, and controlled delegation between AI roles with CrewAI — a foundational skill in modern LLM development.

---

## 📁 File Structure

```text
002-basic-multiagent-crewai-app-content-marketing/
├── main.py                 # Entry point, triggers the crew
├── crew_definition.py      # Main crew logic (avoids circular imports)
├── crew/
│   ├── __init__.py
│   └── crew_config.py      # Imports the crew cleanly for main.py
├── agents/
│   ├── __init__.py
│   ├── online_researcher.py
│   ├── blog_manager.py
│   └── social_media_manager.py
├── tasks/
│   ├── __init__.py
│   ├── research_task.py
│   ├── blog_task.py
│   └── tweet_task.py
├── tools/                  # (optional) for future tool modules
│   └── __init__.py
├── .env                    # Your API keys
├── requirements.txt        # All necessary dependencies
└── README.md               # You're reading it 😊



📌 This CrewAI version mirrors the LangGraph version step-for-step, but simplifies orchestration and modularity.

```

---
