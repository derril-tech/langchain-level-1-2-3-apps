# 🛒 01 - Key Info Extractor from Product Reviews

[👉 Try the Live Demo](https://langchain-level-2-product-review-extractor.streamlit.app/)

This Level 2 LangChain app extracts structured insights from user-written product reviews on e-commerce platforms like Amazon. With just a single pasted review, it can identify **sentiment**, **delivery time**, and **price perception** using OpenAI’s GPT-4o model.

This clean Streamlit-based prototype shows how simple prompt engineering combined with LangChain can convert unstructured text into meaningful key-value pairs — useful in analytics, automation, and feedback systems.

---

## 🧩 Concepts Used

- **Streamlit** — for the lightweight web interface to collect input and display results.
- **LangChain** — to manage the prompt template and flow of user data into the LLM.
- **PromptTemplate** — defines what data to extract and how to ask the LLM to format the output.
- **OpenAI (GPT-4o)** — the underlying LLM performing the actual information extraction.
- **Input validation** — to ensure short enough reviews and that API key is provided.

---

## ▶️ How to Run

1. Clone the repo and navigate into the project directory:

```bash
git clone https://github.com/derril-tech/langchain-level-1-2-3-apps.git
cd langchain-level-1-2-3-apps/level-2/05-review-key-data-extraction
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

You’ll need an OpenAI API key to use the GPT-4o model in this app.

1. Visit [platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)
2. Click “Create new secret key” and copy it (starts with `sk-...`)
3. Paste your key directly into the input field in the Streamlit app when prompted

> 🔒 No `.env` file needed — your key remains local to your session in the browser.

---

## ▶️ Run the App

Once setup is complete, launch the Streamlit app:

```bash
streamlit run main.py
```

This will open a browser window where you can:

- 🔑 **Enter your OpenAI API key**
- 🛍️ **Paste in a product review** (e.g., from Amazon)
- 🤖 **Let GPT-4o extract:**
  - Overall sentiment
  - Delivery duration
  - Price perception
- 📋 **View structured bullet-point output instantly**

## 🛠️ Setup Notes

This project is part of the **LangChain Level 2 Apps Collection**, focused on building hands-on prototypes with interactive user interfaces.

Tech stack and environment:

- **Python 3.11**
- **Streamlit ≥ 1.32**
- **LangChain ≥ 0.1.14**
- **langchain-openai ≥ 0.0.6**
- **OpenAI (GPT-4o model)**

This app highlights practical use of prompt engineering and text extraction logic in real-world scenarios — setting a foundation for more advanced Level 3 LangChain apps.

---

## 📁 File Structure

```text
product-review-extractor/
├── main.py             # Main Streamlit app with UI + GPT-4o integration
├── requirements.txt    # Dependency list (Streamlit, LangChain, OpenAI, etc.)
└── README.md           # You’re reading it
```

> 📌 This project is part of the **LangChain Level 2 Apps** collection.  
> Designed for interactive use, feedback loops, and real-world prototyping.
