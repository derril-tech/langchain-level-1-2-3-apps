# 🧠 11 - RAG with LangSmith Evaluation

This Level 1 LangChain app is a minimal Retrieval-Augmented Generation (RAG) pipeline with evaluation powered by LangSmith. It loads a document, chunks it, stores it in a vector database (FAISS), runs a RAG chain, and evaluates its performance using a LangSmith dataset.

No frontend, no backend — just pure LangChain, OpenAI, and LangSmith in Python.

## 🧩 Concepts Used

- **ChatOpenAI** (gpt-4)
- **OpenAIEmbeddings**
- **FAISS** (in-memory vector store)
- **RecursiveCharacterTextSplitter**
- **Retrieval-Augmented Generation (RAG)**
- **PromptTemplate**
- **LangSmith Client**
- **Evaluation with LangSmith Datasets**
- **StrOutputParser**

## ▶️ How to Run

1. Clone the repo and navigate to the project folder:

   ```bash
   cd level-1/11-rag-basic-langsmith
   ```

2. Install dependencies:

```bash
  pip install -r requirements.txt

```

## 🔐 Setup Your OpenAI Key

Create a `.env` file in the project root and add your OpenAI API key:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

## ▶️ Run the Chatbot

Once your environment and API key are set up, run the script:

```bash
python main.py
```

You should see the document loading logs, chunking output, and one test RAG response printed in the terminal.

If you've connected LangSmith correctly, it will also display evaluation results in your browser via a LangSmith link.
