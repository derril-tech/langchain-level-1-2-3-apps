# 🧠 01 - Conversational RAG with LangChain

This Level 1 LangChain app demonstrates how to build a **Conversational RAG (Retrieval-Augmented Generation)** pipeline that can understand and maintain multi-turn conversations. It starts with a simple RAG setup and progressively evolves to include context-aware questioning, memory persistence, and user session handling.

No frontend. No backend. Just pure Python, LangChain, and OpenAI.

---

## 🧩 Concepts Used

- **ChatOpenAI** (gpt-4o-2024-08-06)
- **TextLoader** and **RecursiveCharacterTextSplitter**
- **OpenAIEmbeddings + Chroma Vector Store**
- **ChatPromptTemplate** with **MessagesPlaceholder**
- **create_stuff_documents_chain**
- **create_retrieval_chain**
- **create_history_aware_retriever**
- **RunnableWithMessageHistory**
- **ChatMessageHistory** for session-based memory

---

## ▶️ How to Run

1. Clone the repo and navigate into the project:

   ```bash
   cd level-1/01-conversational-rag
   ```

````

## 🔐 Setup Your OpenAI Key

Create a `.env` file in the project root and add your OpenAI API key like this:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
````

## ▶️ Run the Chatbot

Once everything is set up, run the script to test the Conversational RAG pipeline:

```bash
python main.py
```

---

## 🛠️ Setup Notes

This project is part of the **LangChain Level 1 Apps Collection** and is designed to demonstrate step-by-step construction of a Conversational RAG pipeline using:

- **LangChain v0.3+**
- **Python 3.11**
- **Pydantic v2**

It shows the evolution from a basic RAG to a memory-aware, session-based conversational agent using traditional LangChain tooling (`create_retrieval_chain`, `create_stuff_documents_chain`, etc.).

Memory is tracked per session ID and is managed in-memory with Python dictionaries, mimicking persistent session behavior.

---

## 📁 File Structure

```text
main.py                     # Entry point containing the entire conversational RAG logic
data/be-good.txt            # Sample document used for retrieval
.env                        # API key (not tracked)
requirements.txt            # Project dependencies
README.md                   # You're reading it
```

---
