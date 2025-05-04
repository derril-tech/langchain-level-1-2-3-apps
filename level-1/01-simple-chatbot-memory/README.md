# 🧠 01 - Simple Chatbot with Memory

This Level 1 LangChain app is a minimal chatbot that uses memory to retain information across user prompts. No frontend, no backend — just pure LangChain + OpenAI via Python.

---

## 🧩 Concepts Used

- **ChatOpenAI** (gpt-4-turbo)
- **ConversationBufferMemory**
- **FileChatMessageHistory**
- **ChatPromptTemplate**
- **LLMChain**

---

## ▶️ How to Run

1. Clone the repo and navigate into the project:
   ```bash
   cd level-1/01-simple-chatbot-memory
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

---

## 🛠️ Setup Notes

This project is part of the **LangChain Level 1 Apps Collection**.

It runs on:

- **Python 3.11**
- **LangChain v0.3+**
- **Pydantic v2**

Memory is stored in `messages.json` (auto-generated after first run).

This project is part of the [LangChain Level 1 Apps](../../README.md).
No frontend or backend — just pure LangChain and Python.

---

## 📁 File Structure

```text
main.py             # Entry point
messages.json       # Conversation memory (auto-created)
.env                # API key (not tracked)
README.md           # You're reading it
requirements.txt    # All dependencies frozen

```
