# 🚀 LangChain Level 1, 2, and 3 Applications

This repository showcases real-world LangChain applications built across three progressive levels of complexity:

- **Level 1 Projects** – standalone applications built purely with LangChain, without any frontend or backend integration
- **Level 2 Projects** – LangChain + UI/API integrations using temporary frontends to test proof of concept
- **Level 3 Projects** – full-stack production-grade applications using Next.js (Frontend on Vercel) and FastAPI (Backend on Render)

These projects demonstrate how to evolve from simple command-line use cases to full-scale, deployable AI-powered systems.

---

## 🧠 What is LangChain?

[LangChain](https://www.langchain.com/) is a powerful framework that simplifies the development of applications using large language models (LLMs). It enables chaining together components such as prompts, memory, retrieval, and agents to build context-aware and dynamic LLM-powered apps.

---

## 🔰 What Do "Level 1", "Level 2", and "Level 3" Mean?

### 🟢 Level 1 – LangChain-Only Apps

Pure LangChain scripts running from the command line. No UI, no backend. Focused on core concepts:

- Memory
- Tools
- Document Loading
- Retrieval (RAG)
- Agents

Ideal for learning and testing individual LangChain modules.

---

### 🟡 Level 2 – LangChain + UI/API Integration

Adds temporary frontend (like Streamlit or simple HTML) and backend (FastAPI, Flask) layers:

- Builds working prototypes
- Ideal for proof of concept apps
- Useful for testing LangChain with APIs or input forms

---

### 🔴 Level 3 – Full Stack LangChain Apps

Full production-ready systems:

- **Frontend:** Next.js (deployed on Vercel)
- **Backend:** FastAPI (deployed on Render)
- **LangChain core:** used via API layer or service architecture
- Often include authentication, agent orchestration, and persistent storage

Best for portfolio-ready, scalable solutions.

---

## 🧪 How to Run Each App

1. Navigate to any project inside the `/level-1/`, `/level-2/` or `/level-3/` folder.
2. Follow the instructions in its own `README.md` to run it.
3. Run the Python file directly:

```bash
cd level-1/01-chatbot-memory
python main.py
```

## 📁 Projects Overview

This repository is organized into three folders:

- `level-1/` – LangChain-only apps (command-line)
- `level-2/` – LangChain + frontend/API integrations (proof of concept)
- `level-3/` – Full-stack LangChain applications (production-grade)

---

### 🟢 Level 1 Projects

| #   | Project Name                        | Link                                                        |
| --- | ----------------------------------- | ----------------------------------------------------------- |
| 1   | Chatbot with Memory                 | [📄 README](./level-1/01-simple-chatbot-memory/README.md)   |
| 2   | Data Extraction Tool                | [📄 README](./level-1/02-key-data-extraction/README.md)     |
| 3   | Sentiment & Political Bias Analyzer | [📄 README](./level-1/03-sentiment-bias-analyzer/README.md) |
| 4   | Database QA System                  | [📄 README](./level-1/04-database-qa/README.md)             |
| 5   | PDF QA Application                  | [📄 README](./level-1/05-pdf-qa/README.md)                  |
| 6   | Large Document Retriever            | [📄 README](./level-1/06-document-retriever/README.md)      |
| 7   | RAG Application                     | [📄 README](./level-1/07-rag-basic/README.md)               |
| 8   | Conversational RAG                  | [📄 README](./level-1/08-rag-conversational/README.md)      |
| 9   | Tool-Using AI Agent                 | [📄 README](./level-1/09-tool-using-agent/README.md)        |
| 10  | LangServe Deployment Demo           | [📄 README](./level-1/10-langserve-deployment/README.md)    |

---

### 🟡 Level 2 Projects

> Proof of Concept apps with UI/API layers

| #   | Project Name        | Link                                                    |
| --- | ------------------- | ------------------------------------------------------- |
| 1   | Text Re-writer      | [📄 README](./level-2/01-text-rewriter/README.md)       |
| 2   | Blog Post Generator | [📄 README](./level-2/02-blog-post-generator/README.md) |

---

### 🔴 Level 3 Projects

> Coming soon — Full-stack LangChain apps using Next.js, FastAPI, and cloud deployment

| #   | Project Name | Link         |
| --- | ------------ | ------------ |
| –   | _TBD_        | _Pending..._ |

## 🛠️ Local Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/derril-tech/langchain-level-1-2-3-apps.git

```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

Make sure your virtual environment is activated, then run:

```bash
pip install -r requirements.txt
```

### 4. Run a Specific Project

Navigate into any project directory and run its main Python script:

```bash
cd level-1/01-chatbot-memory (example)
python main.py
```

## 🙋‍♂️ Author

**Derril Filemon**

- 🔗 [LinkedIn](https://www.linkedin.com/in/derril-filemon-a31715319)
- 🧑‍💻 [GitHub](https://github.com/derril-tech)

---
