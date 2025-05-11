import sqlite3

DB_NAME = 'habit_tracker.db'

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS habits (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                periodicity TEXT NOT NULL,
                creation_date TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS completions (
                id INTEGER PRIMARY KEY,
                habit_id INTEGER,
                completion_date TEXT,
                FOREIGN KEY(habit_id) REFERENCES habits(id)
            )
        ''')
        conn.commit()