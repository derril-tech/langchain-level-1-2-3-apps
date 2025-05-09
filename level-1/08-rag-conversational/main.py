# ========== 1. Load Environment Variables ==========
import os
from dotenv import load_dotenv, find_dotenv

# Load your OpenAI API key from a .env file
_ = load_dotenv(find_dotenv())
openai_api_key = os.environ["OPENAI_API_KEY"]

# ========== 2. Import Core LangChain Tools ==========
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import AIMessage, HumanMessage
from langchain.chains import (
    create_retrieval_chain,
    create_history_aware_retriever,
)
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

# ========== 3. Initialize the Language Model ==========
# Use GPT-4o for better performance
llm = ChatOpenAI(model="gpt-4o-2024-08-06")

# ========== 4. Load and Prepare Text Data ==========
loader = TextLoader("./data/be-good.txt")
docs = loader.load()

# Split text into chunks for vector embedding
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)

# ========== 5. Create a Vector Store ==========
# Embed the text chunks and store them in a vector DB
vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())
retriever = vectorstore.as_retriever()

# ========== 6. Basic Prompt Template (No Chat History) ==========
system_prompt = (
    "You are an assistant for question-answering tasks. "
    "Use the following pieces of retrieved context to answer "
    "the question. If you don't know the answer, say that you "
    "don't know. Use three sentences maximum and keep the "
    "answer concise.\n\n{context}"
)

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}"),
])

# ========== 7. Create Basic RAG Chain (No History) ==========
question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

# Test the basic RAG chain
response = rag_chain.invoke({"input": "What is this article about?"})
print("\nWhat is this article about?\n")
print(response["answer"])

response = rag_chain.invoke({"input": "What was my previous question about?"})
print("\nWhat was my previous question about?\n")
print(response["answer"])

# ========== 8. Add Chat History Awareness ==========
# This helps the system understand follow-up questions better

contextualize_q_system_prompt = (
    "Given a chat history and the latest user question "
    "which might reference context in the chat history, "
    "formulate a standalone question which can be understood "
    "without the chat history. Do NOT answer the question, "
    "just reformulate it if needed and otherwise return it as is."
)

contextualize_q_prompt = ChatPromptTemplate.from_messages([
    ("system", contextualize_q_system_prompt),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}"),
])

# Create a retriever that takes chat history into account
history_aware_retriever = create_history_aware_retriever(
    llm, retriever, contextualize_q_prompt
)

# Prompt that also includes chat history
qa_prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}"),
])

# New chain that supports chat history
question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)
rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)

# ========== 9. Simulate a Chat Session ==========
chat_history = []

question = "What is this article about?"
ai_msg_1 = rag_chain.invoke({"input": question, "chat_history": chat_history})

# Save the exchange in chat history
chat_history.extend([
    HumanMessage(content=question),
    AIMessage(content=ai_msg_1["answer"]),
])

second_question = "What was my previous question about?"
response = rag_chain.invoke({"input": second_question, "chat_history": chat_history})
print("\nWhat was my previous question about?\n")
print(response["answer"])

# ========== 10. Add Session Management (Multiple Users) ==========
# Allows saving separate chat histories using session IDs

store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

conversational_rag_chain = RunnableWithMessageHistory(
    rag_chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history",
    output_messages_key="answer",
)

# Use session ID "001"
response = conversational_rag_chain.invoke(
    {"input": "What is this article about?"},
    config={"configurable": {"session_id": "001"}},
)
print("\nWhat is this article about?\n")
print(response["answer"])

response = conversational_rag_chain.invoke(
    {"input": "What was my previous question about?"},
    config={"configurable": {"session_id": "001"}},
)
print("\nWhat was my previous question about?\n")
print(response["answer"])

# ========== 11. Print Entire Conversation ==========
print("\nConversation History:\n")
for message in store["001"].messages:
    prefix = "AI" if isinstance(message, AIMessage) else "User"
    print(f"{prefix}: {message.content}\n")



# --------------------- CODE NOTES ---------------------
# 1. Environment Variables:
#    We load the OpenAI API key from a .env file so it's not hardcoded in the script.

# 2. Language Model:
#    We use `ChatOpenAI` with the GPT-4o model for improved accuracy and reasoning.

# 3. Document Loading:
#    A `.txt` file is loaded and read into memory. LangChain supports various loaders for PDFs, web pages, etc.

# 4. Text Splitting:
#    We split large texts into smaller chunks to embed and retrieve more effectively. This helps with performance and relevance.

# 5. Embeddings & Vector Store:
#    Each chunk is embedded using OpenAI and stored in a Chroma vector database for fast similarity search.

# 6. Retrieval-Augmented Generation (RAG):
#    Instead of asking the LLM to answer questions from scratch, we retrieve relevant context from our vector store and use that to answer.

# 7. Chat Prompts:
#    We create a structured prompt that guides the LLM’s behavior when responding to questions.

# 8. RAG with Chat History:
#    We simulate conversations and keep track of chat history to handle follow-up questions more intelligently.

# 9. Session Management:
#    This allows each user or session to have its own separate memory using session IDs.

# 10. Final Output:
#    We print answers and show the chat history to see how the model tracks previous questions.

# --------------------- END OF NOTES ---------------------
