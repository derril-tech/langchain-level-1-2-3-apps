# 🧠 02 - Sentiment Analyzer with Structured Output

This Level 1 LangChain app uses OpenAI + LangChain to classify text by **sentiment**, **political tendency**, and **language** — all extracted as structured JSON using a Pydantic schema.

No frontend, no backend — just pure LangChain, OpenAI, and Python.

---

## 🧩 Concepts Used

- **ChatOpenAI** (gpt-4o-2024-08-06)
- **ChatPromptTemplate**
- **Pydantic v2 (BaseModel, Literal)**
- **Structured Output**
- **LangChain Expression Language (Pipe Operator `|`)**

---

## ▶️ How to Run

1. Clone the repo and navigate into the project:

```bash
cd level-1/03-sentiment-bias-analyzer
python main.py
```

## 🔐 Setup Your OpenAI Key

Create a `.env` file and add your OpenAI API key:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxx
```

## ▶️ Run the Extraction app

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
- **OpenAI's GPT-4o model**

All dependencies are frozen in requirements.txt.
This app demonstrates how to extract structured data from user reviews or long-form text.

This project is part of the [LangChain Level 1 Apps](../../README.md).
No frontend or backend — just pure LangChain and Python.

---
