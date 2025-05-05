# Step 1: Load environment variables securely (e.g., your OpenAI API key)
import os
from dotenv import load_dotenv, find_dotenv

# Load the .env file and set environment variables
_ = load_dotenv(find_dotenv())

# Access the OpenAI API key from environment variables
openai_api_key = os.environ["OPENAI_API_KEY"]

# Step 2: Import necessary LangChain and Pydantic v2 components
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from typing import Literal

# Step 3: Create example texts for analysis
trump_follower = (
    "I'm confident that President Trump's leadership and track record will once again "
    "resonate with Americans. His strong stance on economic growth and national security "
    "is exactly what our country needs at this pivotal moment. We need to bring back the "
    "proven leadership that can make America great again!"
)

biden_follower = (
    "I believe President Biden's compassionate and steady approach is vital for our nation "
    "right now. His commitment to healthcare reform, climate change, and restoring our "
    "international alliances is crucial. It's time to continue the progress and ensure a "
    "future that benefits all Americans."
)

# Step 4: Define a basic Classification schema for structured output
class Classification(BaseModel):
    sentiment: str = Field(description="The sentiment of the text")
    political_tendency: str = Field(description="The political tendency of the user")
    language: str = Field(description="The language the text is written in")

# Step 5: Create the prompt template
tagging_prompt = ChatPromptTemplate.from_template(
    """
Extract the desired information from the following passage.

Only extract the properties mentioned in the 'Classification' function.

Passage:
{input}
"""
)

# Step 6: Set up the LLM with structured output (using basic schema)
llm = ChatOpenAI(temperature=0, model="gpt-4o-2024-08-06").with_structured_output(
    Classification
)

# Combine prompt and model into a chain
tagging_chain = tagging_prompt | llm

# Step 7: Analyze Trump supporter text
response = tagging_chain.invoke({"input": trump_follower})
print("\n----------\n")
print("Sentiment analysis Trump follower:")
print("\n----------\n")
print(response)

# Step 8: Analyze Biden supporter text
response = tagging_chain.invoke({"input": biden_follower})
print("\n----------\n")
print("Sentiment analysis Biden follower:")
print("\n----------\n")
print(response)

# Step 9: Redefine schema using stricter enum options with Pydantic v2
class Classification(BaseModel):
    sentiment: Literal["happy", "neutral", "sad"] = Field(
        description="The sentiment of the text"
    )
    political_tendency: Literal["conservative", "liberal", "independent"] = Field(
        description="The political tendency of the user"
    )
    language: Literal["spanish", "english"] = Field(
        description="The language the text is written in"
    )

# Step 10: Re-use the same prompt
tagging_prompt = ChatPromptTemplate.from_template(
    """
Extract the desired information from the following passage.

Only extract the properties mentioned in the 'Classification' function.

Passage:
{input}
"""
)

# Step 11: Update the LLM with the new strict schema
llm = ChatOpenAI(temperature=0, model="gpt-4o-2024-08-06").with_structured_output(
    Classification
)

# Combine updated prompt and model
tagging_chain = tagging_prompt | llm

# Step 12: Analyze Trump supporter again with stricter schema
response = tagging_chain.invoke({"input": trump_follower})
print("\n----------\n")
print("Sentiment analysis Trump follower (with a list of options using enums):")
print("\n----------\n")
print(response)

# Step 13: Analyze Biden supporter again with stricter schema
response = tagging_chain.invoke({"input": biden_follower})
print("\n----------\n")
print("Sentiment analysis Biden follower (with a list of options using enums):")
print("\n----------\n")
print(response)

print("\n----------\n")

######################################################
#  Notes 
######################################################

"""
🧠 LangChain Beginner Notes — Text Classification with Pydantic v2

1. ✅ `dotenv` + `os.environ`: Loads environment variables like your API key securely from a `.env` file.

2. 🧱 `ChatOpenAI`: Connects you to OpenAI’s models (GPT-4o in this case). `temperature=0` makes output deterministic (no randomness).

3. 💬 `ChatPromptTemplate`: Lets you create structured prompts with placeholders (like `{input}`) that can be dynamically replaced.

4. 🧩 `BaseModel` + `Field` (Pydantic v2): Used to define the shape and types of data you want the model to extract. 
   In version 2, `Field(...)` is no longer required for required fields — they are required by default unless given a default value.

5. 🎯 `Literal[...]`: Used in Pydantic v2 to define allowed enum values (e.g., sentiment must be “happy”, “neutral”, or “sad”).

6. 🧠 `.with_structured_output(Classification)`: Tells the model to return results that follow your `Classification` schema exactly. This makes the output predictable and safe to use in production.

7. 🔗 `tagging_prompt | llm`: This is the LangChain "chain" — it connects your prompt to your model in a streamlined pipeline.

8. 📞 `.invoke({...})`: Executes the chain with a given input, letting the LLM respond with structured, schema-conforming output.

This project is a simple but powerful example of building structured text analysis using LangChain + Pydantic v2 + OpenAI — perfect for automating tagging, classification, or even preparing inputs for downstream apps.
"""


"""
🧠 What the Sentiment Analyzer Does
It takes a piece of text (like a political opinion) and extracts three specific attributes using a Large Language Model (LLM):

Sentiment – Whether the overall tone of the text is happy, neutral, or sad.

Political Tendency – The user's likely political leaning: conservative, liberal, or independent.

Language – Whether the text is written in English or Spanish.

These values are extracted using structured output, which means:

The LLM isn't just giving back a free-form answer.

It's responding in a format that matches a Pydantic schema, making the output reliable and easy to parse.

🔍 Step-by-Step Summary of How It Works
You give it a passage (like a quote from a Trump or Biden supporter).

The prompt template tells the LLM to extract only the fields specified in the Classification model.

The Classification schema defines the three properties we care about.

The ChatOpenAI model is configured to use structured output, meaning it will return the response in a format that matches the schema.

The model processes the input and returns an object with three fields: sentiment, political_tendency, and language.

You print and inspect the result.

🛠️ Why It’s Useful
You can plug in any opinion text, and the LLM will extract standardized metadata.

Great for analyzing social media comments, feedback, or political discussions.

Using enum fields (like fixed choices for sentiment or political tendency) keeps the data consistent, clean, and easy to analyze in bulk later.
"""
