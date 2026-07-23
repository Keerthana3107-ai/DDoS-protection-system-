import sqlite3

def init_db():
    conn = sqlite3.connect("ddos.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS request_logs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip_address TEXT,
        request_time TEXT,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()