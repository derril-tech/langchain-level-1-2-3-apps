# app.py

# ============================ #
#      IMPORT DEPENDENCIES    #
# ============================ #

import streamlit as st  # For building the web interface
from langchain import PromptTemplate  # For creating LLM prompts (not used directly here, but commonly part of chains)
from langchain_openai import OpenAI  # LLM wrapper for OpenAI (supports GPT-4o)
from langchain.chains.summarize import load_summarize_chain  # Prebuilt summarization chain
from langchain.text_splitter import RecursiveCharacterTextSplitter  # For splitting long text into manageable chunks
from io import StringIO  # For handling file uploads
import pandas as pd  # Commonly used for file operations (not needed here, included in original)

# ============================================== #
#        FUNCTION TO LOAD OPENAI MODEL (LLM)     #
# ============================================== #

def load_LLM(openai_api_key):
    """
    Loads the OpenAI model using the provided API key.
    Temperature = 0 means it will generate deterministic (less random) responses.
    """
    llm = OpenAI(temperature=0, openai_api_key=openai_api_key)
    return llm


# ============================ #
#         PAGE SETUP          #
# ============================ #

st.set_page_config(page_title="AI Long Text Summarizer")
st.header("AI Long Text Summarizer")

# Intro section split in two columns
col1, col2 = st.columns(2)

with col1:
    st.markdown("🚀 ChatGPT can't summarize long texts easily. Now you can do it with this app using LangChain + GPT-4o!")

with col2:
    st.write("💼 Built by [Derril Filemon](www.linkedin.com/in/derril-filemon-a31715319) — Let’s build your next AI project together!")

# ============================ #
#       API KEY SECTION       #
# ============================ #

st.markdown("## 🔐 Enter Your OpenAI API Key")

def get_openai_api_key():
    return st.text_input(
        label="OpenAI API Key", 
        placeholder="Ex: sk-2twmA8tfCb8un4...", 
        key="openai_api_key_input", 
        type="password"
    )

openai_api_key = get_openai_api_key()

# ============================ #
#        FILE UPLOADER        #
# ============================ #

st.markdown("## 📄 Upload the text file you want to summarize")

uploaded_file = st.file_uploader("Choose a file", type="txt")

# ============================ #
#        OUTPUT SECTION       #
# ============================ #

st.markdown("### 📝 Here is your Summary:")

if uploaded_file is not None:
    # Read file content as a string
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    file_input = stringio.read()

    # Word count safety check
    if len(file_input.split(" ")) > 20000:
        st.error("❌ Please enter a shorter file. The maximum length is 20,000 words.")
        st.stop()

    # API key check
    if not openai_api_key:
        st.warning(
            '⚠️ Please insert your OpenAI API Key. '
            'Instructions [here](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key)'
        )
        st.stop()

    # Split the long text into chunks for processing
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n"],  # First split by double newlines, then by single
        chunk_size=5000,            # Max size of each chunk
        chunk_overlap=350           # Overlap between chunks to maintain context
    )
    splitted_documents = text_splitter.create_documents([file_input])

    # Load the model
    llm = load_LLM(openai_api_key=openai_api_key)

    # Load the summarization chain
    summarize_chain = load_summarize_chain(
        llm=llm,
        chain_type="map_reduce"  # Good for long documents by summarizing chunks and combining results
    )

    # Run the summarization
    summary_output = summarize_chain.run(splitted_documents)

    # Display the result
    st.success("✅ Summary generated successfully!")
    st.write(summary_output)


# ============================================================
# 📘 Explanation for Readers (Not Executed in Streamlit)
# ============================================================

if False:
    """
    • Streamlit is used here to build a web app. `st.file_uploader()` lets the user pick a .txt file.  
    • We read the uploaded file into a string using Python’s `StringIO`.  
    • LangChain's `RecursiveCharacterTextSplitter` splits the long text into smaller overlapping chunks. This is crucial 
      because language models like GPT-4o have token limits.  
    • We use `load_summarize_chain()` from LangChain, which simplifies summarization by using a prebuilt chain type. 
      The `map_reduce` option is perfect for long docs: it first summarizes each chunk (map), then merges them (reduce).  
    • The OpenAI model we load is accessed using `langchain_openai.OpenAI()` — this connects to GPT-4o behind the scenes.  
    • We handle basic error cases like API key not entered or file too long.

    🧪 Learning Tip:  
    Experiment by printing intermediate values like `splitted_documents` to better understand what the app is doing.  
    Tweak the `chunk_size` or `chain_type` and observe the effects. This is how real AI engineers grow!

    📌 Reminder:  
    You are using GPT-4o (gpt-4o-2024-08-06) in this app via LangChain. It's much faster and smarter than older models 
    like GPT-3.5-turbo. But still, keep responses short per chunk if possible.

    ✅ Practice. Make mistakes. Repeat. And debug with confidence!
    """