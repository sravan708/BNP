import sqlite3

# Create/connect database
conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    salary REAL,
    expenses REAL
)
""")

conn.commit()
conn.close()

print("Database created successfully!")