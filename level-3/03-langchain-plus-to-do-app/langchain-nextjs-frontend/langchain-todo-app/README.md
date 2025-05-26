# ✅ 03 - LangChain To-Do App with OpenAI Integration

[👉 Try the Live Demo](https://langchain-level-1-2-3-apps-your-app-link-goes-here.streamlit.app/)

This Level 3 LangChain app enhances a full-stack To-Do application with OpenAI's language capabilities. Built with a FastAPI backend and a Next.js frontend, it allows users to go beyond basic task management by leveraging LLM features like **automatic text summarization** and **poem generation** from to-do items.

This project demonstrates how to orchestrate complex workflows between a modern frontend, a REST API backend, and a LangChain-based language model pipeline — paving the way for building AI-native productivity tools.

---

## 🧩 Concepts Used

- **FastAPI** — for building the backend REST API services.
- **Next.js** — for the modern, interactive frontend.
- **LangChain (v0.1.1)** — used for LLM orchestration via `LLMChain` and `PromptTemplate`.
- **OpenAI (GPT-4 or GPT-4o)** — powers summarization and poem generation features.
- **ORM & SQLite** — used for task data storage and retrieval.
- **Environment Variables** — secure integration of OpenAI API keys.

---

## ▶️ How to Run

1. Clone the repo and navigate into the project directory:

```bash
git clone https://github.com/derril-tech/langchain-level-1-2-3-apps.git
cd langchain-level-1-2-3-apps/level-3/03-langchain-plus-to-do-app
```

2. (Optional) Create and activate a virtual environment:

```bash
pyenv virtualenv 3.11.4 todo-venv
pyenv activate todo-venv
```

3. Install backend dependencies:

```bash
cd 001-langchain-fastapi-backend
pip install -r requirements.txt
```

4. Install frontend dependencies:

```bash
cd ../../langchain-nextjs-frontend/langchain-todo-app
npm ci
```

---

## 🔐 Setup Your OpenAI Key

To enable LLM features (summarize, poem), you need an OpenAI API key.

1. Go to [platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)
2. Copy your API key (starts with `sk-...`)
3. Create a `.env` file in the `backend/` folder:

```env
OPENAI_API_KEY=sk-your-key-here
```

---

## ▶️ Run the App

1. Launch the backend server:

```bash
cd 001-langchain-fastapi-backend
uvicorn main:app --reload
```

2. Launch the frontend app:

```bash
cd ../../002-langchain-nextjs-frontend/langchain-todo-app
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser to use the app.

---

## 🛠️ Setup Notes

This is a Level 3 LangChain app, demonstrating full-stack AI-powered tool integration.

Environment & tech stack:

- **Python 3.11.4**
- **LangChain 0.1.1**
- **OpenAI SDK**
- **FastAPI**
- **Next.js (React 18+)**
- **SQLite + SQLAlchemy ORM**

LangChain and OpenAI features are wired into specific routes (`/summarize-text`, `/write-poem/{id}`) which are called via the frontend. Results (like poems) are displayed in styled UI components.

---

## 📁 File Structure

```text
langchain-todo-app/
├── 001-langchain-fastapi-backend/     # FastAPI + LangChain backend
│   ├── routers/todos.py               # Summarization & poem routes
│   ├── crud.py                        # Database interactions
│   ├── main.py                        # FastAPI app entry
│   └── .env                           # OpenAI key goes here
│
├── 002-langchain-nextjs-frontend/     # Next.js frontend app
│   └── langchain-todo-app/
│       ├── components/todo.js         # Poem UI logic & API integration
│       ├── styles/todo.module.css     # Styled poem popup
│       └── pages/index.js             # To-do app UI
│
└── README.md                          # You're reading it
```

> 📌 This project is part of the **LangChain Level 3 Apps** collection — demonstrating advanced orchestration between LLMs, full-stack frameworks, and user interactivity.
