import sqlite3
from datetime import datetime

DB_PATH = "chat_history.db"

# Create table if not exists
def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS chat_messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Save a single chat message
def save_chat(question: str, answer: str):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        INSERT INTO chat_messages (question, answer, timestamp)
        VALUES (?, ?, ?)
    """, (question, answer, datetime.now().isoformat()))
    conn.commit()
    conn.close()

# Retrieve full chat history
def get_all_chats():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT question, answer, timestamp FROM chat_messages ORDER BY id ASC")
    rows = c.fetchall()
    conn.close()
    return [
        {"question": row[0], "answer": row[1], "timestamp": row[2]}
        for row in rows
    ]
