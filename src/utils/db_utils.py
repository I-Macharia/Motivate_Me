import sqlite3
from pathlib import Path
import hashlib
import os

def init_db():
    """Initialize the SQLite database and create required tables"""
    db_path = Path('src/data/motivate_me.db')
    db_path.parent.mkdir(parents=True, exist_ok=True)
    
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    
    # Create users table
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create chat_history table
    c.execute('''
        CREATE TABLE IF NOT EXISTS chat_history (
            chat_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            message_type TEXT NOT NULL,
            message_content TEXT NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (user_id)
        )
    ''')
    
    conn.commit()
    conn.close()

def get_db_connection():
    """Create a database connection"""
    db_path = Path('src/data/motivate_me.db')
    return sqlite3.connect(db_path)

def hash_password(password: str) -> str:
    """Hash a password for storing"""
    return hashlib.sha256(password.encode()).hexdigest()

def create_user(username: str, password: str, email: str) -> bool:
    """Create a new user"""
    conn = get_db_connection()
    try:
        password_hash = hash_password(password)
        conn.execute(
            'INSERT INTO users (username, password_hash, email) VALUES (?, ?, ?)',
            (username, password_hash, email)
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def verify_user(username: str, password: str) -> int:
    """Verify user credentials and return user_id if valid"""
    conn = get_db_connection()
    try:
        password_hash = hash_password(password)
        cursor = conn.execute(
            'SELECT user_id FROM users WHERE username = ? AND password_hash = ?',
            (username, password_hash)
        )
        result = cursor.fetchone()
        return result[0] if result else None
    finally:
        conn.close()

def save_chat_message(user_id: int, message_type: str, content: str) -> bool:
    """Save a chat message to the database"""
    conn = get_db_connection()
    try:
        conn.execute(
            'INSERT INTO chat_history (user_id, message_type, message_content) VALUES (?, ?, ?)',
            (user_id, message_type, content)
        )
        conn.commit()
        return True
    except sqlite3.Error:
        return False
    finally:
        conn.close()

def get_user_chat_history(user_id: int) -> list:
    """Retrieve chat history for a user"""
    conn = get_db_connection()
    try:
        cursor = conn.execute(
            'SELECT message_type, message_content, timestamp FROM chat_history WHERE user_id = ? ORDER BY timestamp',
            (user_id,)
        )
        return cursor.fetchall()
    finally:
        conn.close()