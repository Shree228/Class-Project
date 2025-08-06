import sqlite3

# Connect to DB
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')

# Add one user
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("admin", "1234"))

conn.commit()
conn.close()

print("✅ Database initialized with default user (admin / 1234)")
