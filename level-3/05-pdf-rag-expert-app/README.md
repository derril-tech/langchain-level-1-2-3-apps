# 📄 05 - PDF Q&A Assistant with File Upload + Chat History

This Level 3 LangChain app lets you upload one or more PDFs, embed them into LanceDB using OpenAI embeddings, and then ask questions in natural language. The app retrieves relevant chunks and uses GPT-4o to answer, with chat history tracking included.

Built with FastAPI + LangServe on the backend and a custom Vite + React + Tailwind frontend, this full-stack project demonstrates end-to-end RAG (Retrieval-Augmented Generation) with file upload, embedding, local vector storage, and persistent chat history.

---

## 🧩 Concepts Used

- **LangChain + LangServe** — for building the RAG pipeline and exposing it via FastAPI routes.
- **LanceDB** — a local-first, on-disk vector database used for storing and searching embedded PDF chunks.
- **OpenAI (GPT-4o)** — the LLM used to answer questions based on retrieved context.
- **Pydantic** — used to define structured input validation for LangServe endpoints.
- **FastAPI** — serves as the backend, handling file uploads, embeddings, and inference requests.
- **React + Vite + Tailwind CSS** — custom frontend with PDF upload, chat UI, and timestamped chat history.
- **SQLite (via `chat_history.db`)** — stores previous user questions and LLM answers across sessions.
- **ChatPromptTemplate** — structured system/human prompt format for more controlled responses.
- **dotenv** — for loading OpenAI API key securely from a `.env` file.

---

## ▶️ How to Run

### 🧪 Backend Setup

1. Clone the repo and navigate to the project folder:

```bash
git clone https://github.com/derril-tech/langchain-level-1-2-3-apps.git
cd langchain-level-1-2-3-apps/level-3/05-pdf-rag-expert-app
```

2. Create and activate the Poetry environment:

```bash
poetry install
poetry shell
```

3. Add your OpenAI API key to a .env file in the app/ folder:

```env
OPENAI_API_KEY=sk-...
```

4. Ingest your PDF file(s):

```bash
python app/ingest.py
```

5. Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

You should see LangServe print something like:

```swift
LANGSERVE: Playground for chain "/rag/" is live at:
           └──> /rag/playground/
```

### 🌐 Frontend Setup

1. Open a second terminal and navigate into the frontend folder:

```bash
cd frontend
```

2. Install dependencies:

```bash
npm install
```

3. Start the Vite development server:

```bash
npm run dev
```

Your frontend will now be available at:
http://localhost:5173

```text

From the browser, you can:

📤 Upload one or more PDF files

❓ Ask questions related to the uploaded documents

🧠 View contextual AI-generated answers

🕒 Review timestamped chat history per session

```

---

## 🔐 Setup Your OpenAI Key

To use GPT-4o, you’ll need an OpenAI API key.

1. Go to [platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)
2. Click “Create new secret key” and copy it (starts with `sk-...`)
3. In your project root, create a `.env` file and add:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

Replace `sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx` with your actual OpenAI API key.
✅ This file is loaded by both the ingestion script and the backend server.

---

## ▶️ Run the Backend and Upload PDFs

Once your environment and `.env` file are ready, follow these steps:

1. **Activate your virtual environment** (if you haven’t already):

```bash
poetry shell
# or
source venv/Scripts/activate  # On Windows with venv
```

2. **Run the backend FastApi server**:

```bash
uvicorn app.main:app --reload
```

You should see LangServe print something like:

```swift
LANGSERVE: Playground for chain "/rag/" is live at:
└──> /rag/playground/
```

3. **Upload a PDF file via the Frontend**
   Use the file uploader on the React page (http://localhost:5173)
   PDFs are embedded using OpenAI embeddings and stored in LanceDB

---

## ▶️ Run the Frontend

The React + Vite frontend allows users to upload PDFs and ask questions interactively.

1. Open a new terminal and navigate to the frontend folder:

```bash
cd frontend
```

3. Start the Vite development server:

```bash
npm run dev
```

4. Open your web browser and navigate to http://localhost:5173

---

```text
🖥️ What You Can Do from the UI
📤 Upload PDFs: Select one or more .pdf files

❓ Ask Questions: Type a question based on your uploaded PDFs

💬 View Chat History: Chat is saved with timestamps locally in SQLite (chat_history.db)
```

---

## 📁 File Structure

```text
05-pdf-rag-expert-app/
├── app/
│   ├── server.py             # FastAPI backend with upload, chat history, LangServe routes
│   ├── rag_chain.py          # LangChain RAG chain setup with LanceDB and OpenAI
│   ├── ingest.py             # PDF chunking, embedding, deduplication logic
│   ├── chat_memory.py        # SQLite-based chat history storage and retrieval
│   └── data/                 # Uploaded PDFs stored here
│
├── .lancedb/                 # LanceDB vector store data (auto-generated)
├── chat_history.db           # SQLite database for chat messages
├── frontend/
│   ├── src/
│   │   ├── App.tsx           # Main React app logic with upload + chat UI
│   │   └── index.css         # Tailwind base styles
│   ├── index.html
│   ├── tailwind.config.cjs   # Tailwind setup (renamed for ES module compatibility)
│   ├── postcss.config.cjs    # PostCSS setup
│   └── package.json
│
├── requirements.txt          # Python dependencies
└── README.md                 # You're reading it
> 📌 🧠 This is a Level 3 LangChain project — combining RAG, vector search, embeddings, and full frontend + backend integration.
```

---
