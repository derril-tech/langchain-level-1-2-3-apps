# -----------------------------
# 📄 TEXT SUMMARIZER APP USING LANGCHAIN + STREAMLIT
# -----------------------------

# Import necessary modules
import streamlit as st  # For creating the web UI
from langchain_openai import OpenAI  # LangChain wrapper for OpenAI LLM
from langchain.docstore.document import Document  # Wrapper to treat each text chunk as a Document
from langchain.text_splitter import CharacterTextSplitter  # To split long text into smaller parts
from langchain.chains.summarize import load_summarize_chain  # Built-in summarization chain

# -----------------------------
# 🚀 FUNCTION TO GENERATE SUMMARY
# -----------------------------
def generate_response(txt, openai_api_key):
    # Initialize the OpenAI model (we use GPT-4o implicitly via API key)
    llm = OpenAI(
        temperature=0,
        openai_api_key=openai_api_key
    )

    # Split the long text into manageable chunks
    text_splitter = CharacterTextSplitter()
    texts = text_splitter.split_text(txt)

    # Convert each chunk into a Document object
    docs = [Document(page_content=t) for t in texts]

    # Load the summarize chain using the "map_reduce" approach
    chain = load_summarize_chain(
        llm,
        chain_type="map_reduce"
    )

    # Run the chain on the documents and return the summary
    return chain.run(docs)

# -----------------------------
# 🌐 STREAMLIT USER INTERFACE
# -----------------------------
# Configure the Streamlit page
st.set_page_config(
    page_title="Writing Text Summarization"
)
st.title("Writing Text Summarization")

# Text area for user to input their long text
txt_input = st.text_area(
    "Enter your text",
    "",
    height=200
)

# Initialize result container
result = []

# Create a form with an API key input and a submit button
with st.form("summarize_form", clear_on_submit=True):
    # Ask user to enter their OpenAI API key
    openai_api_key = st.text_input(
        "OpenAI API Key",
        type="password",
        disabled=not txt_input  # Only enable when there's text
    )

    # Form submission
    submitted = st.form_submit_button("Submit")

    # Check for a valid key and generate the summary
    if submitted and openai_api_key.startswith("sk-"):
        response = generate_response(txt_input, openai_api_key)
        result.append(response)
        del openai_api_key  # Clear key from memory

# Display the summary if available
if len(result):
    st.info(response)


# -----------------------------
# 📘  NOTES BLOCK 
# -----------------------------

if False:
    """
    # 🧠 How This Text Summarizer Works – Beginner Notes

    ## 1. Streamlit:
    - Streamlit makes it easy to build interactive web apps in Python.
    - We use it to let users input text and API keys, then display results on the same page.

    ## 2. LangChain + OpenAI:
    - `OpenAI` from `langchain_openai` is used to access LLMs (like GPT-4o) via your API key.
    - It's wrapped inside LangChain to make building chains like summarization easy.

    ## 3. CharacterTextSplitter:
    - Long text needs to be split before sending it to the LLM, as LLMs have token limits.
    - `CharacterTextSplitter()` divides the input into smaller chunks automatically.

    ## 4. Document Objects:
    - LangChain needs "Document" objects for some of its processing.
    - Each chunk of text is turned into a Document using `Document(page_content=...)`.

    ## 5. Summarize Chain:
    - `load_summarize_chain` loads a ready-to-use summarizer with a method like `map_reduce`.
    - "Map" creates partial summaries of each chunk, "Reduce" combines them into one.

    ## 6. API Key Security:
    - The OpenAI key is input securely and discarded after use for safety.
    - It’s only enabled if the user has entered some text first.

    ## 7. Displaying Output:
    - The final result is shown using `st.info()` only if there's something to show.

    ---

    ✅ Great for learning how to build LLM-powered tools.
    🧪 Try extending it with other chains or using different chain types like 'refine'.
    """