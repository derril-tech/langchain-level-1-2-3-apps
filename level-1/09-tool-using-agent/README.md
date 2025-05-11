# 🤖 01 - LangChain Agent with Tool

This Level 1 LangChain app demonstrates how to build a basic agent that can autonomously decide whether to use an OpenAI LLM (gpt-4o-2024-08-06) or a web search tool (Tavily) to answer user questions. It showcases how to create an agent using LangGraph, stream responses, and store conversational memory using session threads — all with zero frontend or backend, just LangChain and Python.

---

## 🧩 Concepts Used

- **ChatOpenAI** (`gpt-4o-2024-08-06`) – The latest GPT model from OpenAI, used as the core reasoning engine.
- **TavilySearchResults** – A tool for real-time web search to fetch up-to-date answers.
- **create_react_agent** – LangGraph’s built-in agent creator using the ReAct pattern (Reasoning + Acting).
- **HumanMessage** – A message wrapper used to simulate user input into the agent.
- **MemorySaver** – Enables memory persistence so the agent can retain context between turns.
- **thread_id** – Identifies sessions, allowing multiple independent conversations.

---

## ▶️ How to Run

1. Clone the repo and navigate into the project:

```bash
cd level-1/09-tool-using-agent
```

2. (Optional) Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## 🔐 Setup Your OpenAI Key and Tavily API Key

Create a `.env` file in the project root and add your OpenAI API key:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TAVILY_API_KEY=tvly-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

## ▶️ Run the Chatbot

Run the agent script using Python:

```bash
python agent_with_tool.py
```

---

You’ll see multiple printed sections showing:

- **Direct tool invocation results** (e.g., Tavily search).
- **Agent-generated responses** using `.invoke()` and `.stream()`.
- **Memory-based conversations** tracked using `thread_id`.

This lets you observe how the agent autonomously chooses tools, streams answers, and handles conversational context.

---

## 🛠️ Setup Notes

This project is part of the **LangChain Level 1 Apps Collection**.

It demonstrates a working example of LangGraph’s `create_react_agent` pattern, showing how to:

- Combine a chat model (GPT-4o) with external tools (Tavily).
- Let the agent autonomously choose which tool to invoke.
- Stream responses in real time using `.stream()`.
- Retain memory with session-based identifiers (`thread_id`).

This runs on:

- **Python 3.11**
- **LangChain v0.3+**
- **LangGraph**
- **Tavily tool (community integration)**

This project is built for CLI-based exploration. No frontend or backend is included.

---

## 📁 File Structure

```text
agent_with_tool.py     # Main script demonstrating the agent logic
.env                   # API keys for OpenAI and Tavily (not tracked in git)
README.md              # You're reading it
requirements.txt       # Project dependencies
```
