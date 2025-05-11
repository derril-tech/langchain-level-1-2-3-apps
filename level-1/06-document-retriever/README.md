# 🧠 01 - LangChain Vector Search with GPT-4o

This Level 1 LangChain app demonstrates how to embed documents into a vector database and perform semantic searches using OpenAI's GPT-4o. You’ll also learn how to build a simple retrieval-augmented generation (RAG) chain that answers questions using only the provided document context.

No frontend, no backend — just pure LangChain + Python + ChromaDB.

---

## 🧩 Concepts Used

- **ChatOpenAI** (gpt-4o-2024-08-06)
- **Document** (LangChain Core)
- **OpenAIEmbeddings**
- **Chroma** (Vector Store)
- **similarity_search / similarity_search_with_score**
- **Retriever**
- **RunnableLambda**
- **ChatPromptTemplate**
- **RunnablePassthrough**
- **RAG Chain (Retrieval-Augmented Generation)**

---

## ▶️ How to Run

1. Clone the repository and navigate into the project folder:

   ```bash
   cd level-1/06-document-retriever
   ```

---

## 🔐 Setup Your OpenAI Key

Create a `.env` file in the root directory of the project and add your OpenAI API key:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

```

---

## ▶️ Run the Script

Once everything is set up, run the script using:

```bash
python main.py

```

---

## 🛠️ Setup Notes

This project is part of the **LangChain Level 1 Apps Collection** and demonstrates foundational concepts in vector search and retrieval-augmented generation (RAG).

It runs on:

- **Python 3.11+**
- **LangChain v0.3+**
- **ChromaDB**
- **OpenAI Python SDK**

There’s no frontend or backend — just a standalone Python script showcasing LangChain’s core capabilities with GPT-4o.

---

## 📁 File Structure

```text
main.py             # Entry point: loads docs, embeds them, runs searches and chains
.env                # Contains your OpenAI API key (not tracked by Git)
requirements.txt    # All required dependencies
README.md           # You're reading it

```

---
