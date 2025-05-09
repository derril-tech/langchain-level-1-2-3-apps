# 🧠 01 - Basic RAG Application with LangChain

This Level 1 LangChain app demonstrates a Retrieval-Augmented Generation (RAG) pipeline that enables answering questions based on content from a local document. The focus is on building a simple but effective backend-only system — no UI, no API, just LangChain and OpenAI working together to retrieve and reason over text.

---

## 🧩 Concepts Used

- **ChatOpenAI** (gpt-4o-2024-08-06)
- **TextLoader** (for loading raw text files)
- **RecursiveCharacterTextSplitter** (splits long text into chunks)
- **OpenAIEmbeddings** (transforms text into vectors)
- **Chroma** (vector database for storing and querying embeddings)
- **Retriever** (fetches relevant chunks from the vector store)
- **ChatPromptTemplate** (formats the prompt for the LLM)
- **RunnablePassthrough & RunnableParallel** (LangChain components for chaining logic)
- **StrOutputParser** (extracts final string from the LLM output)

---

## ▶️ How to Run

1. Clone the repo and navigate into the project folder:

```bash
cd level-1/02-basic-rag-application
```

## 🔐 Setup Your OpenAI Key

Create a `.env` file in the project root and add your OpenAI API key like this:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

## ▶️ Run the Script

Run the script using Python:

```bash
python main.py
```

---

## 🛠️ Setup Notes

This project is part of the **LangChain Level 1 Apps Collection**.

It runs on:

- **Python 3.11+**
- **LangChain v0.3+**
- **ChromaDB**
- **Pydantic v2**

This basic RAG implementation uses a single `.txt` file and demonstrates how to split it into chunks, embed it, and retrieve relevant parts to answer user questions.

No frontend or backend — just pure LangChain and Python.

---

## 📁 File Structure

```text
main.py             # Entry point with the full RAG pipeline
data/be-good.txt    # Source document to query
.env                # Stores your OpenAI API key (not tracked)
README.md           # You're reading it
requirements.txt    # All dependencies

```

---
