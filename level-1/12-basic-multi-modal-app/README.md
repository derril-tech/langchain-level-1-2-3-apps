# 🧠 12 - Multi-Modal PDF RAG App (LangChain + GPT-4o)

This Level 1 LangChain app is a simple Multi-Modal Retrieval-Augmented Generation (RAG) tool that extracts and analyzes text, tables, and images from a PDF using LangChain, GPT-3.5, and GPT-4o.

It supports:

- Text & table summarization via GPT-3.5
- Image summarization via GPT-4o Vision
- Contextual querying using LangChain’s MultiVectorRetriever
- A lightweight Streamlit UI to ask questions about the document

No backend. No database. Just pure LangChain magic.

---

## 🧩 Concepts Used

- **LangChain MultiVectorRetriever** – enables retrieval from multiple sources (text, tables, images)
- **ChromaDB** – lightweight in-memory vector store
- **InMemoryStore** – stores raw content linked to vector summaries
- **partition_pdf (Unstructured)** – parses text, tables, and images from PDFs
- **GPT-3.5** – used for summarizing text and tables
- **GPT-4o (Vision)** – used for summarizing embedded images
- **Streamlit** – UI layer for user interaction

---

## ▶️ How to Run

1. Clone the repo and navigate into the project:

```bash
git clone https://github.com/derril-tech/langchain-level-1-apps.git
cd level-1/12-basic-multi-modal-app
```

2. Install dependencies:

````bash
pip install -r requirements.txt


## 🔐 Setup Your OpenAI Key

Create a `.env` file in the root of the project and add your OpenAI API key:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
````

## ▶️ Run the Chatbot

You can run the app in two ways:

### 🧪 Option 1: Run the backend logic and test in terminal

```bash
python main.py
```

This extracts text, tables, and images from the PDF, summarizes each with GPT-3.5 and GPT-4o, and performs a sample RAG query.

### 🖥️ Option 2: Launch the Streamlit UI

```bash
streamlit run app.py

```

This opens a web UI where you can type questions about your PDF and see the multi-modal responses.

## 🛠️ Setup Notes

This project is part of the **LangChain Level 1 Apps Collection** and is designed to demonstrate how to build a functional multi-modal RAG app using minimal tooling.

It runs on:

- **Python 3.11**
- **LangChain v0.3+**
- **Pydantic v2**
- **OpenAI GPT-3.5 + GPT-4o (Vision)**
- **Unstructured for PDF parsing**
- **Streamlit for UI (optional)**

You’ll also need:

- **Poppler** and **Tesseract** installed on your system for PDF and image parsing (especially on Windows).
- A test PDF containing text, tables, and images.

---

## 📁 File Structure

```text
main.py                             # End-to-end PDF parser, summarizer, and RAG pipeline
app.py                              # Streamlit UI for querying the summarized content
startupai-financial-report-v2.pdf   # Sample multimodal PDF (text + tables + images)
figures/                            # Auto-generated folder for extracted images
.env                                # OpenAI API key (excluded from Git)
requirements.txt                    # All dependencies
README.md                           # You're reading it

```

---
