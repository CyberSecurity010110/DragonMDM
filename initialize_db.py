import sqlite3

def initialize_database():
    conn = sqlite3.connect('data/devices.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS devices (
        device_id TEXT PRIMARY KEY,
        user_name TEXT,
        os_version TEXT,
        manufacturer TEXT,
        model TEXT,
        last_seen TIMESTAMP
    )
    ''')
    conn.commit()
    conn.close()
    print("Database initialized successfully.")

if __name__ == "__main__":
    initialize_database()
