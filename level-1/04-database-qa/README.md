# 🧠 04 - Natural Language to SQL (LangChain + SQLite)

This Level 1 LangChain app lets you ask questions in plain English and get answers from a local SQLite database. It converts your question into SQL using GPT-4o, runs the query, and then summarizes the result using the same LLM.

No frontend, no backend — just pure LangChain + OpenAI + SQLite in Python.

---

## 🧩 Concepts Used

- **ChatOpenAI** (gpt-4o)
- **SQLDatabase** (reads schema from SQLite)
- **PromptTemplate**
- **StrOutputParser**
- **QuerySQLDatabaseTool**
- **RunnablePassthrough**

---

## ▶️ How to Run

1. Clone the repo and navigate into the project:

```bash
cd level-1/04-database-qa
```

---

## 🔐 Setup Your OpenAI Key

Create a `.env` file in the root directory and add your OpenAI API key:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxx
```

---

## ▶️ Run the App

Make sure your virtual environment is activated, then run:

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
- **OpenAI GPT-4o**

The app reads schema info directly from the SQLite database and uses the LLM to convert natural language questions into valid SQL. It then runs the SQL and summarizes the result using the same model.

This project is part of the [LangChain Level 1 Apps](../../README.md).
No frontend or backend — just pure LangChain and Python.

---

## 📁 File Structure

```text
main.py                   # Entry point with SQL question → execution → summary logic
data/street_tree_db.sqlite  # SQLite database used for querying
.env                      # API key (not tracked)
README.md                 # You're reading it
requirements.txt          # All dependencies for this app

```

---
