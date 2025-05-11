# Import required libraries
import streamlit as st  # For creating the web UI
from langchain import PromptTemplate  # To structure the prompt
from langchain_openai import OpenAI  # OpenAI wrapper for LangChain

# -------------------------
# Define the prompt template
# -------------------------
template = """\
For the following text, extract the following information:

sentiment: Is the customer happy with the product? 
Answer Positive if yes, Negative if not, Neutral if either, or Unknown if unknown.

delivery_days: How many days did it take for the product to arrive? 
If this information is not found, output No information about this.

price_perception: How does the customer feel about the price? 
Answer Expensive, Cheap, Neutral, or Unknown.

Format the output as bullet points:
- Sentiment
- How long took it to deliver?
- How was the price perceived?

Input example:
This dress is pretty amazing. It arrived in two days, just in time for my wife's anniversary present. 
It is cheaper than the other dresses out there, but I think it is worth it for the extra features.

Output example:
- Sentiment: Positive
- How long took it to deliver? 2 days
- How was the price perceived? Cheap

text: {review}
"""

# Initialize a LangChain PromptTemplate
prompt = PromptTemplate(
    input_variables=["review"],  # Variable placeholder in the template
    template=template,
)

# -------------------------
# Function to load the LLM
# -------------------------
def load_LLM(openai_api_key):
    """
    Load the OpenAI LLM with zero temperature for deterministic output.
    """
    llm = OpenAI(temperature=0, openai_api_key=openai_api_key)
    return llm

# -------------------------
# Streamlit UI Setup
# -------------------------
st.set_page_config(page_title="Extract Key Information from Product Reviews")
st.header("Extract Key Information from Product Reviews")

# Split screen with instructions and link
col1, col2 = st.columns(2)

with col1:
    st.markdown("Extract the following from a product review:")
    st.markdown("- Sentiment\n- How long did it take to deliver?\n- How was the price perceived?")

with col2:
    st.write("\nContact [Derril Filemon](www.linkedin.com/in/derril-filemon-a31715319) to build your AI Projects")

# -------------------------
# Input: OpenAI API Key
# -------------------------
st.markdown("## Enter Your OpenAI API Key")

def get_openai_api_key():
    return st.text_input(
        label="OpenAI API Key", 
        placeholder="Ex: sk-2twmA8tfCb8un4...", 
        key="openai_api_key_input", 
        type="password"
    )

openai_api_key = get_openai_api_key()

# -------------------------
# Input: Product Review
# -------------------------
st.markdown("## Enter the Product Review")

def get_review():
    return st.text_area(
        label="Product Review", 
        label_visibility='collapsed', 
        placeholder="Paste your product review here...", 
        key="review_input"
    )

review_input = get_review()

# Optional: Warn if the review is too long
if len(review_input.split(" ")) > 700:
    st.warning("Please enter a shorter product review (max 700 words).")
    st.stop()

# -------------------------
# Output: Display extracted data
# -------------------------
st.markdown("### Key Data Extracted:")

if review_input:
    if not openai_api_key:
        st.warning(
            'Please insert your OpenAI API Key. '
            'Instructions [here](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key)', 
            icon="⚠️"
        )
        st.stop()

    # Load the language model
    llm = load_LLM(openai_api_key=openai_api_key)

    # Insert the user review into the prompt
    prompt_with_review = prompt.format(review=review_input)

    # Ask the model to extract key data
    key_data_extraction = llm(prompt_with_review)

    # Display the extracted results
    st.write(key_data_extraction)

# -------------------------
# 🧠 Optional:  Notes Block (Hidden in App but kept for reference)
# -------------------------
if False:
    """
    ################## 🧠 LangChain Beginner Notes: Product Review Extractor ##################

    1. import streamlit / langchain / openai:
       We import the tools for building the UI (Streamlit), prompt structuring (PromptTemplate), and the OpenAI wrapper for LangChain.

    2. PromptTemplate:
       This defines the structure of what we want the language model to do with the input. It tells the LLM how to extract sentiment, delivery time, and price perception.

    3. load_LLM():
       This function loads and initializes the GPT-4o language model using the OpenAI API key and sets temperature to 0 (for consistent results).

    4. Streamlit UI:
       We use Streamlit to collect input: OpenAI key and product review. It also shows the final extracted data in a clean format.

    5. Error Handling:
       We check for max word count (700) and show a warning if the API key is missing.

    6. Formatting Prompt:
       We inject the review into the prompt using `prompt.format()` and then send that to the model using `llm(prompt_with_review)`.

    7. Output:
       We display the model's response clearly under the header “Key Data Extracted.”

    This is a great starting point for NLP apps using LangChain + OpenAI. From here, you can scale it up to batch process multiple reviews or save output to a database!

    ##########################################################################################
    """
