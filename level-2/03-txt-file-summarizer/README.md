# 📄 03 - AI Long Text Summarizer (TXT File)

[👉 Try the Live Demo](https://langchain-level-1-2-3-apps-6wjnccdrjksrnu8uowdskg.streamlit.app/)

This Level 2 LangChain app allows users to upload a `.txt` file and instantly generate a high-quality summary of its contents using GPT-4o.

The app features a simple Streamlit interface and utilizes LangChain's built-in summarization chains with smart chunking logic. It’s designed to handle long texts while enforcing word count limits and providing clean summaries even for large enterprise documents.

---

## 🧩 Concepts Used

- **Streamlit** — to build the web UI and handle file uploads.
- **LangChain** — to structure the summarization logic and call OpenAI models.
- **RecursiveCharacterTextSplitter** — splits long documents into overlapping chunks.
- **load_summarize_chain (map_reduce)** — for multi-step summarization workflows.
- **OpenAI (GPT-4o)** — processes each chunk and combines them into a final summary.
- **Input validation** — enforces file size limits and checks for missing API keys.

---

## ▶️ How to Run

1. Clone the repo and navigate into the project directory:

```bash
git clone https://github.com/derril-tech/langchain-level-1-2-3-apps.git
cd langchain-level-1-2-3-apps/level-2/03-txt-file-summarizer
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
- 📤 Upload a .txt file (max 20,000 words)
- 🧠 Summarize the document using GPT-4o and LangChain
- 📃 View your final summary instantly in the app

## 🛠️ Setup Notes

This project is part of the **LangChain Level 2 Apps Collection** — designed for hands-on learning with real-world tools.

Tech stack and environment:

- **Python 3.11**
- **Streamlit ≥ 1.32**
- **LangChain ≥ 0.1.14**
- **langchain-openai ≥ 0.0.6**
- **OpenAI (GPT-4o model)**

This app introduces concepts like recursive text splitting, error handling, and chain abstraction for summarizing long content — setting you up for more advanced Level 3 workflows.

---

## 📁 File Structure

```text
txt-summarizer/
├── app.py              # Main Streamlit app with UI + summarization logic
├── requirements.txt    # Dependency list (LangChain, Streamlit, OpenAI)
└── README.md           # You're reading it
```

> 📌 This project is part of the **LangChain Level 2 Apps** collection.  
> Designed for interactive use, feedback loops, and real-world prototyping.
