# app/chat_memory.py
from datetime import datetime
from typing import List, Dict

# In-memory chat store
chat_history: List[Dict[str, str]] = []

def save_chat(question: str, answer: str):
    """Save a single question-answer pair with timestamp."""
    chat_history.append({
        "timestamp": datetime.utcnow().isoformat(),
        "question": question,
        "answer": answer
    })

def get_chat_history() -> List[Dict[str, str]]:
    """Return the full chat history (in memory)."""
    return chat_history
