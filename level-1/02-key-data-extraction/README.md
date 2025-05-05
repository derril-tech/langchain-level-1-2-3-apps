# 🧠 02 - Data Extraction with LangChain

This Level 1 LangChain app demonstrates how to extract structured information (like name, lastname, and country) from unstructured text using LangChain, OpenAI, and Pydantic v2.

No frontend, no backend — just pure LangChain + OpenAI via Python.

---

## 🧩 Concepts Used

- **ChatOpenAI** (`gpt-4o-2024-08-06`)
- **Pydantic v2** models for structured output
- **ChatPromptTemplate**
- **Structured Output Parsing**
- **LangChain Chain Composability**

---

## ▶️ How to Run

1. Clone the repo and navigate into the project:

   ```bash
   cd level-1/02-key-data-extraction
   ```

````

## 🔐 Setup Your OpenAI Key

Create a `.env` file and add your OpenAI API key:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxx
````

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

All dependencies are frozen in requirements.txt.

This app demonstrates how to extract structured data from user reviews or long-form text.

This project is part of the [LangChain Level 1 Apps](../../README.md).
No frontend or backend — just pure LangChain and Python.

---

## 📁 File Structure

```text
main.py             # Entry point with entity extraction logic
.env                # OpenAI key (not committed to version control)
README.md           # You’re reading it
requirements.txt    # All dependencies listed

```
