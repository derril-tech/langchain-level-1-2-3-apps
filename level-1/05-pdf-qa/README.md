# 🧠 02 - PDF Q&A with RAG

This Level 1 LangChain app loads a PDF file, splits it into chunks, stores them in a vector database, and uses Retrieval-Augmented Generation (RAG) to answer questions based on the document content. No frontend, no backend — just LangChain + OpenAI running in Python.

---

## 🧩 Concepts Used

- **ChatOpenAI** (`gpt-4o-2024-08-06`)
- **PyPDFLoader**
- **RecursiveCharacterTextSplitter**
- **OpenAIEmbeddings**
- **Chroma Vectorstore**
- **ChatPromptTemplate**
- **Retrieval Chain (RAG)**
- **create_stuff_documents_chain**

---

## ▶️ How to Run

1. Clone the repository and navigate into the project directory:

   ```bash
   cd level-1/02-pdf-qa
   ```

   ***

## 🔐 Setup Your OpenAI Key

Create a `.env` file in the project root and add your OpenAI API key:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## ▶️ Run the Script

Once your environment is set up and dependencies installed, run the script:

```bash
python main.py
```

---

## 🛠️ Setup Notes

This project is part of the **LangChain Level 1 Apps Collection**.

It runs on:

- **Python 3.11+**
- **LangChain v0.3+**
- **Pydantic v2**
- **Chroma for vector storage**
- **OpenAI GPT-4o model**

The app demonstrates a full RAG pipeline using PDF input, chunking, embeddings, retrieval, and LLM-based answering — all in under 100 lines of code.

---

## 📁 File Structure

```text
main.py             # Entry point: loads PDF, builds retriever, runs question-answering
.env                # Stores your OpenAI API key (not tracked)
requirements.txt    # Frozen dependencies
README.md           # You're reading it
/data/Be_Good.pdf   # Sample PDF document for testing

```

---
