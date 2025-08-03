# 🧠 03 - CrewAI Researcher: Multi-Agent Insights by Business Domain

This Level 4 AI Agent project uses **CrewAI** to simulate a collaborative content marketing team — powered by OpenAI’s GPT-4o. It’s a refactored version of the original LangGraph implementation but built using CrewAI’s declarative multi-agent orchestration framework.

This fullstack multi-agent LangChain app lets users select emerging technologies (like AI Agents, RPA Bots, or Generative AI) and explore how they apply across business areas like Marketing, HR, Sales, or Support.

Built with a clean Vite + React UI styled using Mantine, the app launches a backend CrewAI multi-agent workflow that returns structured results — including blog articles and YouTube videos relevant to each business area.

---

## 🧩 Concepts Used

- **Vite + React (TypeScript)** — for a blazing-fast modern frontend with component-based structure.
- **Mantine** — elegant UI framework for styling inputs, cards, typography, and layouts.
- **Lucide Icons** — beautiful Feather-style icon system used with Mantine components.
- **CrewAI (LangGraph)** — multi-agent orchestration for autonomous task delegation and research.
- **FastAPI** — Python backend that handles the research logic and serves API endpoints.
- **Polling mechanism** — frontend periodically checks backend for updated agent results.
- **Normalization logic** — raw backend JSON is transformed into structured frontend-friendly output.
- **React Hooks** — especially useState, useEffect, and a custom useCrewOutput() hook for state + API logic.
- **react-hot-toast** — for real-time user feedback (e.g., job launched, error, completed).

---

## ▶️ How to Run

1.  Clone the repo and navigate to the project folder:

```bash
git clone https://github.com/derril-tech/langchain-level-1-2-3-apps.git
cd langchain-level-1-2-3-apps/level-4-AI-Agents/003-crewai-fullstack-multiagent-app

```

2. Install the backend dependencies and run the FastAPI server:

```bash
cd backend
pip install -r requirements.txt
uvicorn server:app --reload --port 3001

```

This starts the Vite development server and opens the app in your default browser at http://localhost:5173.

3. Open a second terminal, go to the frontend folder and install dependencies:

```bash
cd ../frontend-vite
npm install

```

4. Run the Vite + React frontend:

```bash
npm run dev

```

This will launch the app at: http://localhost:5173/
Make sure the backend is running at: http://localhost:3001/

```text
Once both servers are running, you can:

🧠 Choose AI technologies and business areas
🛰️ Launch the CrewAI multi-agent research process
📡 Watch logs stream in real-time
✅ View a structured summary of blog articles and YouTube videos
```

---

## 🔐 Setup Your OpenAI Key

This app requires access to OpenAI’s GPT-4o model.

1. Visit [platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)
2. Copy your API key (it starts with `sk-...`)
3. Create a `.env` in your backend folder file in the project root with the following contents:

```env
OPENAI_API_KEY=your_openai_key_here
YOUTUBE_API_KEY=your_youtube_key_here
SERPER_API_KEY=your_serper_key_here    # Optional: for enhanced web search
```

🛡️ Your keys remain local and secure inside the .env file and are never exposed online.
💡 The backend uses this key to run multi-agent research tasks via the OpenAI API using GPT-4o.

---

## 🛠️ Setup Notes

This project is part of the **LangChain Level 4 AI Agents Collection** — demonstrating how to combine:

🧠 AI agent coordination (CrewAI)
🌐 Full-stack architecture (FastAPI backend + React frontend)
🎨 Clean design and status visibility (Mantine + event polling)

Tech stack:

FRONTEND:

- **React + Vite**
- **Mantine UI components**
- **TypeScript**
- **Lucide icons**
- **React Hot Toast for notifications**

BACKEND:

- **FastAPI with LangChain + CrewAI**
- **OpenAI GPT-4o model**
- **REST endpoints for task orchestration and result polling**
- **Lucide icons**

AGENT LOGIC:

- **CrewAI orchestrates multiple agents with memory and roles**
- **Results are grouped by business area and returned as structured JSON**

> 🧪 This project is designed to teach agent design, state modeling, and controlled delegation between AI roles with CrewAI — a foundational skill in modern LLM development.
> 💡 Designed for fast iteration and deployment, with clean code separation and strong typing.

---

## 📁 File Structure

```text
003-crewai-fullstack-multiagent-app/
├── backend/
│   ├── main.py               # FastAPI app with /api/multiagent and polling endpoints
│   ├── crew/                 # CrewAI agent configuration and orchestration
│   │   └── research_manager.py
│   ├── models.py             # Pydantic models for request/response types
│   └── utils.py              # Helper functions for normalizing results
│
├── frontend-vite/
│   ├── index.html            # HTML entry point for Vite
│   ├── src/
│   │   ├── main.tsx          # Mounts <App /> inside root div
│   │   ├── App.tsx           # Main component that renders input, log, output
│   │   ├── layout.tsx        # Global layout with metadata + header
│   │   ├── components/
│   │   │   ├── Header.tsx        # Gradient topbar with title
│   │   │   ├── InputSection.tsx  # Technology/business input with Mantine
│   │   │   ├── EventLog.tsx      # Live polling log display
│   │   │   └── FinalOutput.tsx   # Renders blog and video links
│   │   ├── hooks/
│   │   │   └── useCrewOutput.tsx # Handles API interaction and polling
│   │   └── styles/
│   │       └── App.css       # Legacy Vite styles (can be removed)
│   └── vite.config.ts        # Vite + TypeScript config
│
└── README.md                 # You’re reading it

📌 This project is part of the LangChain Level 4 Apps collection — showcasing full-stack AI agent orchestration from UI to backend.

```

---
