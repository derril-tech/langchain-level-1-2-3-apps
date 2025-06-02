# ✅ PDF Manager App with LangChain & OpenAI Integration

[👉 Try the Live Demo](https://pdf-manager-app.vercel.app/)

This advanced full-stack application allows users to upload, store, and interact with PDFs using powerful AI features. Built using a FastAPI backend and a Next.js frontend, the app integrates **LangChain**, **OpenAI**, and **FAISS** to offer functionalities like **PDF summarization** and **question answering** through LLM orchestration.

It extends the base PDF Manager app—previously powered by Google Cloud Storage (GCS) and PostgreSQL—by layering in intelligent document processing and a user-friendly interface.

---

## 🧩 Concepts Used

- **FastAPI** — Backend API server.
- **Next.js** — Interactive frontend.
- **Google Cloud Storage** — For storing uploaded PDF files.
- **PostgreSQL** — Stores metadata and links.
- **LangChain (v0.1.1)** — Orchestration of summarization and RAG pipelines.
- **OpenAI (GPT-4 or GPT-4o)** — Summarization and QA model.
- **FAISS** — Vector database for document retrieval.
- **PyPDFLoader** — PDF parsing utility.
- **RecursiveCharacterTextSplitter** — For text chunking and embedding.
- **Environment Variables** — Secure integration of API and database credentials.

---

## ▶️ How to Run

1. Clone the repository and navigate to the root directory:

```bash
git clone https://github.com/your-org/pdf-manager-app-langchain.git
cd pdf-manager-app-langchain
```

2. Set up Python virtual environment and install backend dependencies:

```bash
cd backend
pyenv virtualenv 3.11.4 pdf-manager-venv
pyenv activate pdf-manager-venv
pip install -r requirements.txt
```

3. Install frontend dependencies:

```bash
cd ../frontend/pdf-manager-app
npm ci
```

---

## 🔐 Setup Your API Keys

Create a `.env` file in the `backend/` directory with the following:

```env
OPENAI_API_KEY=sk-your-key-here
GOOGLE_APPLICATION_CREDENTIALS=./secrets/gcs-key.json
GCP_BUCKET_NAME=pdf-manager-app-bucket
DATABASE_URL=postgresql://derril:filemon@host:port/mypdfdatabase
```

Ensure the service key file exists at the path specified.

---

## ▶️ Run the App

1. Start the backend server:

```bash
cd backend
uvicorn main:app --reload
```

2. Start the frontend:

```bash
cd ../frontend/pdf-manager-app
npm run dev
```

Visit [http://localhost:3000](http://localhost:3000) in your browser.

---

## 🛠️ Setup Notes

This app enhances traditional file upload functionality with AI-powered features:

- **PDF Summarization**: Route `/summarize-text` powered by LangChain LLMChain.
- **Question Answering**: Route `/qa-pdf/{id}` uses RAG over PDFs stored in GCS.

---

## 📁 File Structure

```text
pdf-manager-app-langchain/
├── backend/                         # FastAPI + LangChain backend
│   ├── routers/pdfs.py              # Summarization & QA routes
│   ├── crud.py                      # Upload & DB logic
│   ├── main.py                      # App entry point
│   └── .env                         # API and DB credentials
│
├── frontend/pdf-manager-app/       # Next.js frontend
│   ├── components/                 # Question input and display
│   └── pages/index.js              # PDF upload, selection, QA input
│
└── README.md                       # You're reading it
```

> 📌 This is a Level 3 AI-powered application that showcases end-to-end orchestration using LangChain, LLMs, and full-stack frameworks.
