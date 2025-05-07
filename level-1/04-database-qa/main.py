import os
from dotenv import load_dotenv, find_dotenv

# Load OpenAI API key from .env
_ = load_dotenv(find_dotenv())
openai_api_key = os.environ["OPENAI_API_KEY"]

# LangChain imports
from langchain_openai import ChatOpenAI
from langchain_community.utilities import SQLDatabase
from langchain_community.tools import QuerySQLDatabaseTool
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# Initialize LLM
llm = ChatOpenAI(model="gpt-4o-2024-08-06")

# Connect to SQLite DB
sqlite_db_path = "data/street_tree_db.sqlite"
db = SQLDatabase.from_uri(f"sqlite:///{sqlite_db_path}")
schema = db.get_table_info()

# SQL generation prompt (STRICT)
sql_prompt = PromptTemplate.from_template(
    """Given the user's question and the database schema, generate ONLY a valid SQL query.
Do NOT include explanations, comments, or markdown formatting. Only output raw SQL.

Schema:
{schema}

Question: {question}

SQL:"""
)

write_query_chain = sql_prompt | llm | StrOutputParser()
execute_query_tool = QuerySQLDatabaseTool(db=db)

# Question to ask
question = "List the species of trees that are present in San Francisco"

# Generate SQL
sql_query = write_query_chain.invoke({"question": question, "schema": schema})
sql_query = sql_query.strip().strip("`").replace("```sql", "").replace("```", "").strip()
print("\nGenerated SQL Query:\n", sql_query)

# Execute SQL
query_result = execute_query_tool.invoke({"query": sql_query})
print("\nRaw SQL Result:\n", query_result)

# Final answer generation prompt (NO schema)
answer_prompt = PromptTemplate.from_template(
    """Given the following user question, SQL query, and SQL result, provide a clear and concise answer.

Question: {question}
SQL Query: {query}
SQL Result: {result}
Answer:"""
)

# Run final LLM chain
final_response_chain = answer_prompt | llm | StrOutputParser()
response = final_response_chain.invoke({
    "question": question,
    "query": sql_query,
    "result": query_result
})

print("\n----------\n")
print("Final Answer:")
print("\n----------\n")
print(response)
print("\n----------\n")


"""
 NOTES:

🌱 .env File and API Key
We use a `.env` file to store our OpenAI API key so we don’t hardcode secrets into the code. `load_dotenv()` loads the key safely.

🧠 ChatOpenAI
This class is how LangChain connects to OpenAI’s GPT models. We specify which model we want to use (e.g., "gpt-4o").

💾 SQLDatabase
This LangChain utility allows us to connect to an SQLite database using its file path. The database schema is automatically read.

🧾 PromptTemplate
We create a template that tells the LLM what kind of SQL query to generate. This gives the model a clear, consistent format to follow.

🔁 RunnablePassthrough and .assign()
These tools help us build a chain of steps. We assign intermediate values like the generated SQL and its result before passing them further down the chain.

🧪 QuerySQLDataBaseTool
This tool takes SQL text and runs it against the connected database, returning the result (like rows from a table).

🧩 Chain Structure
We break the problem into three steps:
    1. Convert question ➜ SQL
    2. SQL ➜ Execute in DB
    3. SQL + Result ➜ Final Answer

🧼 StrOutputParser
We use this to clean the LLM’s output and get a readable string.

📌 Summary:
With this code, a user can type a natural language question like:
    "List the species of trees in San Francisco"
...and the system will:
    - Create a valid SQL query,
    - Run that query on your database,
    - Give a human-friendly answer using GPT.

This is a clean and modern LangChain Level 1 pipeline that connects language, logic, and data.
"""
