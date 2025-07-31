# 🧠 01 - Multi-Agent Content Marketing Team (LangGraph + GPT-4o)

This Level 4 LangChain project demonstrates a full **multi-agent AI system** using LangGraph, designed to replicate a real-world **content marketing team**. Powered by OpenAI’s GPT-4o and structured with LangGraph, this system simulates a manager delegating tasks to agents who perform research, blog writing, and tweet generation.

Each agent performs a role like a human team member:

- 🧠 **Online Researcher** — gathers insights from the web.
- ✍️ **Blog Manager** — turns research into polished blog content.
- 📣 **Social Media Manager** — creates engaging social posts.

Built for backend execution in Python, this prototype shows how AI agents can collaborate within a workflow graph to complete complex tasks without human help.

---

## 🧩 Concepts Used

- **LangGraph** — the core framework for building multi-agent workflows using nodes, edges, and memory state.
- **LangChain** — provides tools for creating intelligent agents with tool use, prompts, and function routing.
- **AgentExecutor** — wraps each AI agent with memory, tools, and decision logic.
- **ChatOpenAI (GPT-4o)** — the large language model powering all agent actions and decisions.
- **TavilySearch & Custom Web Scraper** — tools that enable real-time research and web data extraction.
- **StateGraph** — LangGraph’s engine to route logic between agents based on conditions and outputs.
- **Prompt Engineering** — carefully designed system prompts help guide each agent’s role (researcher, writer, social media).

---

## ▶️ How to Run

1. Clone the repo and navigate into the project directory:

```bash
git clone https://github.com/derril-tech/langchain-level-1-apps.git
cd langchain-level-1-apps/level-4-AI-Agents/001-basic-multiagent-app-content-marketing
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
This will start the multi-agent workflow:

🤖 The Content Marketing Manager decides who should act next.

🌐 The Online Researcher gathers information from the web.

📝 The Blog Manager transforms the research into an SEO-optimized article.

🐦 The Social Media Manager generates a concise tweet to share the content.

You’ll see printed outputs for each agent’s message, along with separator lines to indicate each completed task in the workflow.

📌 This is a backend CLI-based app. For a UI version, consider using Streamlit or a LangChain frontend.

```

---

## 🛠️ Setup Notes

This project is part of the **LangChain Level 4 AI Agents Collection** — focusing on building structured, multi-role workflows powered by state graphs and conditional routing.

Tech stack and environment:

- **Python 3.11**
- **LangChain ≥ 0.1.14**
- **LangGraph ≥ 0.0.20**
- **langchain-openai ≥ 0.0.6**
- **langchain-community ≥ 0.0.23**
- **OpenAI (GPT-4o model)**
- **Tavily Search Tool (optional)**
- **BeautifulSoup4** — for scraping page content
- **python-dotenv** — for securely loading API keys

> 🧪 This project is designed to teach agent design, state modeling, and controlled delegation between AI roles — a foundational skill in modern LLM development.

---

## 📁 File Structure

```text
001-basic-multiagent-app-content-marketing/
├── main.py             # Core Python script that defines all agents and the LangGraph workflow
├── .env                # Stores your OpenAI and Tavily API keys securely (not committed to Git)
├── requirements.txt    # Python dependencies for running the project
└── README.md           # You're reading it 😊


📌 This project is part of the LangChain Level 4 AI Agents collection.
Designed to simulate real-world team automation with agents communicating via LangGraph workflows.

```

---
