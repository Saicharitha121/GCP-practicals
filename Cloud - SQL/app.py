### CLOUD SQL -- python code to connect to mysql database


import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

conn = mysql.connector.connect(
    host=os.getenv('DB_HOST', '127.0.0.1'),
    port=int(os.getenv('DB_PORT', 3308)),
    user=os.getenv('DB_USER', 'charitha-user'),
    password=os.getenv('DB_PASSWORD', 'Charitha@123'),
    database=os.getenv('DB_NAME', 'charidb')
)

cursor = conn.cursor()
cursor.execute("SELECT NOW();")
result = cursor.fetchone()

print("Connected Successfully", result)

# cursor.execute("""
# INSERT INTO customers (name, email) VALUES
# ('John Doe', 'johndoe@example.com'),
# ('Jane Smith', 'janesmith@example.com');
#                """)

# conn.commit()

cursor.execute("SELECT * FROM students;")
for row in cursor.fetchall():
    print(row)
cursor.close()
conn.close()
