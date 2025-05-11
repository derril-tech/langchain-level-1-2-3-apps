# Text Rewriter App using LangChain, Streamlit, and OpenAI's GPT-4o

# ---------------------
# Import required libraries
# ---------------------
import streamlit as st
from langchain import PromptTemplate
from langchain_openai import OpenAI

# ---------------------
# Define a prompt template with tone and dialect conversion
# ---------------------
template = """
    Below is a draft text that may be poorly worded.
    Your goal is to:
    - Properly redact the draft text
    - Convert the draft text to a specified tone
    - Convert the draft text to a specified dialect

    Here are some examples of different Tones:
    - Formal: Greetings! OpenAI has announced that Sam Altman is rejoining the company...
    - Informal: Hey everyone, it's been a wild week! We've got some exciting news...

    Dialect examples:
    - American: French Fries, apartment, garbage, cookie, parking lot
    - British: chips, flat, rubbish, biscuit, car park

    Please start the redaction with a warm introduction.

    Below is the draft text, tone, and dialect:
    DRAFT: {draft}
    TONE: {tone}
    DIALECT: {dialect}

    YOUR {dialect} RESPONSE:
"""

# Create a LangChain PromptTemplate using the variables in our prompt
prompt = PromptTemplate(
    input_variables=["tone", "dialect", "draft"],
    template=template,
)

# ---------------------
# Load the OpenAI LLM (GPT-4o)
# ---------------------
def load_LLM(openai_api_key):
    """Initializes the OpenAI LLM with the provided API key."""
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    return llm

# ---------------------
# Set up the Streamlit app layout
# ---------------------
st.set_page_config(page_title="Re-write your text")
st.header("Re-write your text")

# Introductory text
col1, col2 = st.columns(2)
with col1:
    st.markdown("Re-write your text in different styles.")
with col2:
    st.write("Contact [Derril Filemon](www.linkedin.com/in/derril-filemon-a31715319) to build your AI Projects.")

# ---------------------
# Get OpenAI API key input from the user
# ---------------------
st.markdown("## Enter Your OpenAI API Key")
def get_openai_api_key():
    return st.text_input(
        label="OpenAI API Key",
        placeholder="Ex: sk-2twmA8tfCb8un4...",
        key="openai_api_key_input",
        type="password"
    )

openai_api_key = get_openai_api_key()

# ---------------------
# Get the text to re-write from the user
# ---------------------
st.markdown("## Enter the text you want to re-write")
def get_draft():
    return st.text_area(
        label="Text",
        label_visibility='collapsed',
        placeholder="Your Text...",
        key="draft_input"
    )

draft_input = get_draft()

# Optional: enforce a max word limit to avoid excessive prompt cost or API errors
if len(draft_input.split(" ")) > 700:
    st.warning("Please enter a shorter text. The maximum length is 700 words.")
    st.stop()

# ---------------------
# Get tone and dialect preferences
# ---------------------
col3, col4 = st.columns(2)

with col3:
    option_tone = st.selectbox(
        'Which tone would you like your redaction to have?',
        (
            'Formal',
            'Informal',
            'Humorous',
            'Persuasive',
            'Empathetic'
        )
    )

with col4:
    option_dialect = st.selectbox(
        'Which English Dialect would you like?',
        ('American', 'British')
    )



# ---------------------
# Generate and display rewritten text
# ---------------------
st.markdown("### Your Re-written text:")

if draft_input:
    if not openai_api_key:
        st.warning(
            'Please insert OpenAI API Key. Instructions [here](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key)',
            icon="⚠️"
        )
        st.stop()

    # Load the language model
    llm = load_LLM(openai_api_key=openai_api_key)

    # Format the prompt with user input
    prompt_with_draft = prompt.format(
        tone=option_tone,
        dialect=option_dialect,
        draft=draft_input
    )

    # Generate the rewritten response
    improved_redaction = llm(prompt_with_draft)

    # Show the result
    st.write(improved_redaction)

# =========================
# Teaching Notes (For Developers Only — Not Rendered in App)
# =========================

# BEGINNER NOTES:
#
# 1. Streamlit:
#    Streamlit is a Python tool for building web apps using simple Python scripts. Great for prototyping!
#
# 2. LangChain:
#    LangChain helps manage prompts, language model logic, and integrations with LLMs like GPT-4o.
#
# 3. PromptTemplate:
#    This lets you insert variables (like draft text, tone, dialect) into a reusable prompt.
#
# 4. OpenAI LLM (GPT-4o):
#    A powerful language model. We access it using the `OpenAI()` class, and it needs your API key.
#
# 5. load_LLM():
#    A helper function that creates the LLM instance with your OpenAI API key and chosen randomness level (`temperature=0.7`).
#
# 6. st.text_area(), st.selectbox(), etc.:
#    These are Streamlit UI elements that let users type input, pick dropdown options, and see results.
#
# 7. prompt.format():
#    Replaces `{draft}`, `{tone}`, and `{dialect}` in the prompt with your actual values to prepare the final input for GPT-4o.
#
# 8. Why check word limits?
#    GPT-4o (or any OpenAI model) has token limits. Keeping user inputs short helps prevent errors and keeps the app responsive.
#
# TIP:
# - Always start with small inputs and test.
# - Read prompt responses carefully.
# - Fine-tune the template for your specific use case.
