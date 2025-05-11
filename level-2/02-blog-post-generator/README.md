# 📝 Blog Post Generator with Streamlit + LangChain

[👉 Try the Live Demo](https://your-app-url.streamlit.app/) <!-- Replace with actual link if needed -->

This Level 2 LangChain app allows users to generate a complete 400-word blog post by simply entering a topic. It’s powered by OpenAI’s `gpt-4o` model and demonstrates real-world use of LangChain’s prompt templating inside a clean and responsive Streamlit interface.

With just a topic and an API key, users can trigger the generation of a full post — followed by a word count summary — simulating a powerful writing assistant tailored for content creators and startup blogs.

---

## 🧩 Concepts Used

- **Streamlit** — for building the interactive web app interface.
- **LangChain** — to manage prompt formatting and LLM calls.
- **PromptTemplate** — to dynamically insert user-provided topics into a reusable blog generation prompt.
- **OpenAI (GPT-4o)** — the powerful language model used to generate long-form content.
- **User input validation** — basic check to ensure the OpenAI key is present and formatted correctly before triggering generation.

---

## ▶️ How to Run

1. Clone the repo and navigate into the project directory:

```bash
git clone https://github.com/derril-tech/langchain-level-1-2-3-apps.git
cd langchain-level-1-2-3-apps/level-2/02-blog-post-generator
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

You’ll need an OpenAI API key to use the GPT-4o model for blog generation.

1. Go to [platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)
2. Create or copy your API key (it starts with `sk-...`)
3. Paste it directly into the app's sidebar input when prompted

> 🔒 This version does **not** require a `.env` file. The key is securely entered via the Streamlit interface and stays local to your session.

---

## ▶️ Run the App

Once everything is set up, launch the Streamlit app using the following command:

```bash
streamlit run main.py
```

This will open a local browser window where you can:

- 🔑 Enter your OpenAI API key
- 📝 Type in a topic (e.g., “The Future of AI in Education”)
- 🚀 Instantly generate a 400-word blog post with a word count summary

## 🛠️ Setup Notes

This project is part of the **LangChain Level 2 Apps Collection** — focused on building real-world prototypes with functional user interfaces.

Environment and tech stack:

- **Python 3.11**
- **Streamlit ≥ 1.32**
- **LangChain ≥ 0.1.14**
- **langchain-openai ≥ 0.0.6**
- **OpenAI (GPT-4o model)**

This app emphasizes simplicity while teaching core LangChain concepts — including LLM invocation, prompt templating, and minimal UI logic using Python.

---

## 📁 File Structure

```text
blog-generator/
├── main.py             # Main Streamlit app with UI and LangChain logic
├── requirements.txt    # Dependency list (Streamlit, LangChain, OpenAI)
└── README.md           # You're reading it
```

> 📌 This project is part of the **LangChain Level 2 Apps** collection.  
> Designed for interactive use, feedback loops, and real-world prototyping.
