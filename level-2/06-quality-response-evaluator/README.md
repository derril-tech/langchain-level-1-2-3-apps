# 📊 01 - Quality of Response Evaluator for RAG Apps

[👉 Try the Live Demo](https://langchain-level-1-2-3-apps-q75wp2a2etewd8swerkmad.streamlit.app/)

This Level 2 LangChain app evaluates how well a RAG (Retrieval-Augmented Generation) application performs by comparing its answers to known correct responses — powered by GPT-4o.

Built with a clean Streamlit UI, this tool demonstrates how to assess response accuracy using **LangChain’s QAEvalChain** with real document context. Upload a `.txt` file, ask a question, provide the expected answer, and let the app determine whether the AI-generated response is correct.

---

## 🧩 Concepts Used

- **Streamlit** — for building a responsive and user-friendly web interface.
- **LangChain** — to create both the retrieval-based QA system and the evaluation pipeline.
- **RetrievalQA** — retrieves relevant chunks from the document and passes them to the LLM for answering.
- **FAISS** — fast vector store for storing and searching document embeddings.
- **OpenAI (GPT-4o)** — the language model used for both answering and evaluating questions.
- **QAEvalChain** — lets an LLM compare the generated answer to the ground truth to evaluate quality.

---

## ▶️ How to Run

1. Clone the repo and navigate into the project directory:

```bash
git clone https://github.com/derril-tech/langchain-level-1-2-3-apps.git
cd langchain-level-1-2-3-apps/level-2/06-quality-response-evaluator
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
2. Copy your API key (starts with `sk-...`)
3. Paste it directly into the app when prompted

> 🔒 Your key is only used locally in your Streamlit session and is not saved or exposed anywhere.

## ▶️ Run the App

Once setup is complete, launch the Streamlit app:

```bash
streamlit run main.py
```

This will open a browser window where you can:

- 🔑 Enter your OpenAI API key
- 📄 Upload a .txt document
- ❓ Enter a fact-checked question
- ✅ Provide the correct answer
- 🤖 Let GPT-4o answer and evaluate the result using LangChain’s QAEvalChain

## 🛠️ Setup Notes

This project is part of the **LangChain Level 2 Apps Collection** — focused on building real-world AI tools with UIs and evaluation logic.

Tech stack and environment:

- **Python 3.11**
- **Streamlit ≥ 1.32**
- **LangChain ≥ 0.1.14**
- **langchain-openai ≥ 0.0.6**
- **OpenAI GPT-4o model**

This app introduces foundational concepts like vector search, document chunking, and using LLMs to evaluate other LLM responses — making it a strong stepping stone toward advanced Level 3 LangChain apps.

## 📁 File Structure

```text
quality-response-evaluator/
├── main.py             # Main Streamlit app with UI + RAG + evaluation logic
├── requirements.txt    # Dependency list (LangChain, Streamlit, OpenAI)
└── README.md           # You're reading it
```

> 📌 This project is part of the **LangChain Level 2 Apps** collection.  
> Designed for interactive use, feedback loops, and real-world prototyping.
