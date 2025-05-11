# 🧠 01 - Text Summarizer with LangChain + GPT-4o

[👉 Try the Live Demo](https://langchain-level-1-2-3-apps-49mp6omqdwbwsaosrxlach.streamlit.app/)

This Level 2 LangChain app summarizes long-form text into short, digestible summaries using GPT-4o.

With a clean Streamlit interface and a LangChain-powered backend, this prototype demonstrates how to chunk long text, process it through an LLM, and deliver meaningful summaries — great for articles, documents, or research material.

---

## 🧩 Concepts Used

- **Streamlit** — for creating the interactive user interface.
- **LangChain** — to orchestrate the summarization chain.
- **CharacterTextSplitter** — to split long inputs into manageable chunks.
- **Document** — wraps each chunk to work with LangChain chains.
- **OpenAI (GPT-4o)** — used as the LLM via API for summarizing.
- **Summarize Chain (MapReduce)** — breaks up and combines partial summaries from the LLM.

---

## ▶️ How to Run

1. Clone the repo and navigate into the project directory:

```bash
git clone https://github.com/derril-tech/langchain-level-1-2-3-apps.git
cd langchain-level-1-2-3-apps/level-2/04-text-summarizer
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

Once everything is set up, launch the Streamlit app using the following command:

```bash
streamlit run main.py
```

This will open a local browser window where you can:

- 🔑 Enter your OpenAI API key
- 📄 Paste any long-form text into the input box
- ⚙️ Let the app process and summarize the text using GPT-4o
- 📘 View the generated summary right below the form

## 🛠️ Setup Notes

This project is part of the **LangChain Level 2 Apps Collection** — designed to help you build interactive AI tools with real-world utility.

Environment & Tech Stack:

- **Python 3.11**
- **Streamlit ≥ 1.32**
- **LangChain ≥ 0.1.14**
- **langchain-openai ≥ 0.0.6**
- **OpenAI GPT-4o model**

This app showcases core LangChain patterns such as chain loading, document chunking, and prompt orchestration — ideal preparation before jumping into more complex Level 3 agent-based applications.

## 📁 File Structure

```text
text-summarizer/
├── main.py             # Streamlit app with UI and summarization logic
├── requirements.txt    # Dependency list (LangChain, Streamlit, OpenAI)
└── README.md           # You're reading it
```

> 📌 This project is part of the **LangChain Level 2 Apps** collection.  
> Designed for interactive use, feedback loops, and real-world prototyping.
