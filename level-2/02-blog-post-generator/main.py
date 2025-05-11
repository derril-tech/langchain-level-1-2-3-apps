# ========================================
# 📘 Streamlit + LangChain Blog Generator
# ========================================

# Import necessary modules
import streamlit as st
from langchain_openai import OpenAI  # This gives us access to GPT models via OpenAI
from langchain import PromptTemplate  # This helps us create prompt templates dynamically

# -------------------------------
# 🧱 Streamlit UI Configuration
# -------------------------------

# Set the configuration for the Streamlit app (page title)
st.set_page_config(page_title="Blog Post Generator")

# Title displayed on the main page
st.title("📝 Blog Post Generator")

# Sidebar input for the OpenAI API key (hidden input for security)
openai_api_key = st.sidebar.text_input("🔑 Enter your OpenAI API Key", type="password")

# -------------------------------
# 🔁 LangChain + OpenAI Function
# -------------------------------

# Function to generate blog post based on a given topic
def generate_response(topic):
    # Initialize OpenAI language model (uses gpt-4o automatically via langchain_openai if available)
    llm = OpenAI(openai_api_key=openai_api_key)

    # Create a prompt template to instruct the LLM on the blog's format and content
    template = """
    As an experienced startup and venture capital writer, 
    generate a 400-word blog post about {topic}.
    
    Your response should be in this format:
    First, print the blog post.
    Then, sum the total number of words and print it like this: 
    This post has X words.
    """

    # Use LangChain's PromptTemplate to insert the topic into the prompt
    prompt = PromptTemplate(
        input_variables=["topic"],  # Tell LangChain which variables we will be replacing
        template=template
    )

    # Fill in the prompt with the user-entered topic
    query = prompt.format(topic=topic)

    # Send the prompt to the OpenAI LLM and get the response
    response = llm(query, max_tokens=2048)

    # Display the result in the Streamlit app
    return st.write(response)

# -------------------------------
# 🧠 User Input + Logic
# -------------------------------

# Main input box where user types the blog topic
topic_text = st.text_input("📌 Enter the topic for your blog post:")

# Validate that the API key starts with "sk-" (basic OpenAI key format check)
if not openai_api_key.startswith("sk-"):
    st.warning("⚠️ Please enter a valid OpenAI API Key to continue.")
elif topic_text:
    # Only generate blog post if both API key and topic are present
    generate_response(topic_text)

# ============================================================
# 📘 Explanation for Readers
# ============================================================

if False:
    """
    🔰  NOTES - HOW THIS APP WORKS

    1. **Imports**:
       - `streamlit`: Handles the UI.
       - `langchain_openai.OpenAI`: Wrapper to use GPT-4o from OpenAI via LangChain.
       - `PromptTemplate`: Allows dynamic prompt construction.

    2. **Streamlit UI**:
       - The page is titled and styled using `st.set_page_config()` and `st.title()`.
       - The sidebar is used for secure entry of the OpenAI API key.

    3. **LangChain Function**:
       - The `generate_response()` function initializes the `OpenAI` class with your key.
       - A custom template is created asking GPT to write a blog post and count its words.
       - The template is formatted with the user’s topic, sent to GPT-4o, and displayed with `st.write()`.

    4. **Conditional Logic**:
       - The app checks whether a valid OpenAI API key is present before making a call.
       - It also ensures that the topic field is not empty before submitting a request.

    5. **LLM Used**:
       - This app uses `gpt-4o-2024-08-06` via LangChain's OpenAI wrapper (most up-to-date and cost-efficient model as of 2025).

    🛠️ TIP: 
    Use this as a base for more advanced blog generation features — like tone selection, word count sliders, or keyword targeting.

    📌 PRACTICE:
    Try tweaking the prompt or the output length, or even add options for blog post format. Streamlit + LangChain is great for learning while building.
    """
