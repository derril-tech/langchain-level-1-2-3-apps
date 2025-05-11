# 🧠 02 - Text Rewriter with Tone & Dialect Control

[👉 Try the Live Demo](https://langchain-level-1-2-3-apps-q75wp2a2etewd8swerkmad.streamlit.app/)

This Level 2 LangChain app allows users to rewrite informal or unclear text into more polished versions using different tones and dialects — powered by OpenAI’s GPT-4o.

Built with a clean Streamlit UI, this prototype demonstrates real-world prompt engineering with interactive controls. Choose between tones like Formal, Informal, Humorous, Persuasive, or Empathetic — and rewrite in American or British English.

---

## 🧩 Concepts Used

- **Streamlit** — for building the interactive web app interface.
- **LangChain** — to manage the dynamic prompt template and chain structure.
- **PromptTemplate** — lets us inject tone, dialect, and user input into a flexible prompt format.
- **OpenAI (GPT-4o)** — the language model that rewrites the user’s text.
- **User input validation** — basic check to avoid overly long text submissions.

---

## ▶️ How to Run

1. Clone the repo and navigate into the project directory:

```bash
git clone https://github.com/derril-tech/langchain-level-1-2-3-apps.git
cd langchain-level-1-2-3-apps/level-2/text-rewriter
```

2. (Optional) Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## 🔐 Setup Your OpenAI Key

You’ll need an OpenAI API key to use GPT-4o.

1. Go to [platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)
2. Copy your key (starts with `sk-...`)
3. Paste it directly into the app when prompted — no need for a `.env` file in this Streamlit version.

> 🔒 Your key stays local to your session in the Streamlit app.

---

## ▶️ Run the App

Once everything is set up, launch the Streamlit app:

```bash
streamlit run main.py
```

This will open a local browser window where you can:

- 🔑 Enter your OpenAI API key
- 📝 Paste in a draft sentence or paragraph
- 🎨 Select a tone (e.g., Formal, Humorous, Persuasive, Empathetic, etc.)
- 🌍 Choose your preferred English dialect (American or British)
- 🚀 Get a rewritten version instantly from GPT-4o

## 🛠️ Setup Notes

This project is part of the **LangChain Level 2 Apps Collection** — which focuses on building interactive prototypes with user interfaces.

Tech stack and environment:

- **Python 3.11**
- **Streamlit ≥ 1.32**
- **LangChain ≥ 0.1.14**
- **langchain-openai ≥ 0.0.6**
- **OpenAI (GPT-4o model)**

This app introduces more advanced prompt design, UI layout with columns, and external input (API key) handling — preparing you for Level 3 app development.

---

## 📁 File Structure

```text
text-rewriter/
├── main.py             # Main Streamlit app with UI + LLM logic
├── requirements.txt    # Dependency list (LangChain, Streamlit, OpenAI)
└── README.md           # You're reading it
```

> 📌 This project is part of the **LangChain Level 2 Apps** collection.  
> Designed for interactive use, feedback loops, and real-world prototyping.
