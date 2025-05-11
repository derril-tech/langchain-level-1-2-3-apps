# Import necessary libraries
import streamlit as st
from langchain_openai import OpenAI  # LangChain wrapper for OpenAI models
from langchain.text_splitter import CharacterTextSplitter  # To split large texts
from langchain_community.embeddings import OpenAIEmbeddings  # Embedding model
from langchain_community.vectorstores import FAISS  # Vector storage using FAISS
from langchain.chains import RetrievalQA  # Chain to answer questions from documents
from langchain.evaluation.qa import QAEvalChain  # Chain to evaluate question-answer quality

# Main function that handles response generation and evaluation
def generate_response(uploaded_file, openai_api_key, query_text, response_text):
    # Step 1: Read the uploaded .txt file
    documents = [uploaded_file.read().decode()]  # Decode bytes to string

    # Step 2: Split the text into manageable chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.create_documents(documents)

    # Step 3: Generate embeddings using OpenAI
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

    # Step 4: Store the text chunks in a FAISS vector database
    db = FAISS.from_documents(texts, embeddings)

    # Step 5: Create a retriever interface from the FAISS vector store
    retriever = db.as_retriever()

    # Step 6: Construct the real QA pair for evaluation
    real_qa = [{"question": query_text, "answer": response_text}]

    # Step 7: Build the QA retrieval chain using the retriever
    qachain = RetrievalQA.from_chain_type(
        llm=OpenAI(openai_api_key=openai_api_key),
        chain_type="stuff",
        retriever=retriever,
        input_key="question"
    )

    # Step 8: Generate predictions (LLM responses to the questions)
    predictions = qachain.apply(real_qa)

    # Step 9: Create a QA evaluation chain using LLM-as-a-judge
    eval_chain = QAEvalChain.from_llm(llm=OpenAI(openai_api_key=openai_api_key))

    # Step 10: Evaluate how close the prediction is to the real answer
    graded_outputs = eval_chain.evaluate(
        real_qa,
        predictions,
        question_key="question",
        prediction_key="result",
        answer_key="answer"
    )

    # Return both prediction and evaluation result
    return {"predictions": predictions, "graded_outputs": graded_outputs}


# Streamlit UI setup
st.set_page_config(page_title="Evaluate a RAG App")
st.title("Evaluate a RAG App")

# Expandable explanation panel
with st.expander("Evaluate the quality of a RAG APP"):
    st.write("""
        To evaluate the quality of a RAG app, we will
        ask it questions for which we already know the
        real answers.

        That way we can see if the app is producing
        the right answers or if it is hallucinating.
    """)

# File uploader for .txt file
uploaded_file = st.file_uploader(
    "Upload a .txt document",
    type="txt"
)

# Question input
query_text = st.text_input(
    "Enter a question you have already fact-checked:",
    placeholder="Write your question here",
    disabled=not uploaded_file
)

# Correct answer input
response_text = st.text_input(
    "Enter the real answer to the question:",
    placeholder="Write the confirmed answer here",
    disabled=not uploaded_file
)

# Initialize result list
result = []

# Form for submitting the OpenAI key and starting evaluation
with st.form("myform", clear_on_submit=True):
    openai_api_key = st.text_input(
        "OpenAI API Key:",
        type="password",
        disabled=not (uploaded_file and query_text)
    )
    submitted = st.form_submit_button(
        "Submit",
        disabled=not (uploaded_file and query_text)
    )
    if submitted and openai_api_key.startswith("sk-"):
        with st.spinner("Wait, please. I am working on it..."):
            response = generate_response(
                uploaded_file,
                openai_api_key,
                query_text,
                response_text
            )
            result.append(response)
            del openai_api_key  # Clear key for security

# Display evaluation results
if len(result):
    st.write("Question")
    st.info(response["predictions"][0]["question"])

    st.write("Real answer")
    st.info(response["predictions"][0]["answer"])

    st.write("Answer provided by the AI App")
    st.info(response["predictions"][0]["result"])

    st.write("Therefore, the AI App answer was")
    st.info(response["graded_outputs"][0]["results"])


# ------------------------- #
# READER NOTES  #
# ------------------------- #

if False:
    """
    READER NOTES (LangChain Quality of Response Evaluator)
    ------------------------------------------------------------------

    1. What is RAG?
       - RAG stands for Retrieval-Augmented Generation. It combines document retrieval with generative AI.
       - The LLM first retrieves relevant info from documents before generating an answer.

    2. Why Evaluate a RAG App?
       - LLMs can give different answers to the same question.
       - We need to check if the AI gives accurate, grounded answers — not hallucinations.

    3. What is a Vector Store (FAISS)?
       - A vector store indexes document embeddings so that relevant chunks can be retrieved quickly based on similarity.

    4. What is RetrievalQA?
       - A LangChain tool that ties together retrieval and question-answering using an LLM.

    5. What is QAEvalChain?
       - A chain that lets an LLM evaluate the quality of another LLM’s answer — an “LLM as a judge”.

    6. Why use Streamlit?
       - Streamlit creates quick and interactive web UIs with just Python.

    7. What is `gpt-4o-2024-08-06`?
       - A powerful and efficient multimodal version of GPT-4, used here to generate and evaluate answers.

    8. How to Improve This App?
       - Add support for multiple questions.
       - Log results to a file.
       - Use different evaluation prompts for nuanced grading.

    Summary:
    This app lets you upload a document, ask a known question, compare the AI's answer to a real one,
    and see if the AI “gets it right”. It’s a perfect demo of LangChain’s RetrievalQA + QAEvalChain capabilities.
    """
