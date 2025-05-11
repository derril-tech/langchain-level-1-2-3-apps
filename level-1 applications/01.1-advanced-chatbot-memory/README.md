# 🧠 02 - Advanced ChatBot Memory & Sessions

This Level 1 LangChain app demonstrates how to build a stateful chatbot using LangChain's message history and session memory system. You’ll learn how to differentiate between sessions, recall user inputs, and implement a limited memory window.

---

## 🧩 Concepts Used

- **ChatOpenAI** (gpt-4-turbo)
- **ChatMessageHistory** (per-session memory)
- **RunnableWithMessageHistory** (wraps chain with memory logic)
- **ChatPromptTemplate** with **MessagesPlaceholder**
- **Limited memory logic** (last-N-message retention)
- **Multiple user sessions** with custom `session_id`s

---

## ▶️ How to Run

1. Clone the repo and navigate into the project:
   ```bash
   cd level-1/01.1-advanced-chatbot-memory
   ```

## 🔐 Setup Your OpenAI Key

Create a `.env` file and add your OpenAI API key:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxx
```

## ▶️ Run the Chatbot

```bash
python main.py
```

## 🛠️ Setup Notes

This project is part of the **LangChain Level 1 Apps Collection**.

It runs on:

- **Python 3.11**
- **LangChain v0.3+**
- **Pydantic v2**
- **dotenv for environment config**

Memory is handled fully in-memory via ChatMessageHistory — no files are created, but sessions are identified by session_id.

This project is part of the [LangChain Level 1 Apps](../../README.md).
No frontend or backend — just pure LangChain and Python.

## 📁 File Structure

```text
main.py             # Main chatbot logic with memory + session demos
.env                # API key (not tracked)
README.md           # You're reading it
requirements.txt    # All dependencies

```
