import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = "charidb"

print("✅ Environment variables loaded")

conn = mysql.connector.connect(
    host=DB_HOST,
    port=int(DB_PORT),
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)

print("✅ Connected to Cloud SQL")

cursor = conn.cursor()

students = [
    ("Sai Charitha", "saicharitha@gmail.com", 21),
    ("Ananya", "ananya@gmail.com", 22)
]

insert_query = """
INSERT INTO users (name, email, age)
VALUES (%s, %s, %s)
"""

cursor.executemany(insert_query, students)
conn.commit()

print("✅ Data inserted")

cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
print("✅ Connection closed")
