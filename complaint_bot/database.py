import sqlite3

DB_PATH = "db.sqlite3"

def create_table():
   connection = sqlite3.connect(DB_PATH)
   cursor = connection.cursor()
   cursor.execute("""
      CREATE TABLE IF NOT EXISTS complaints (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         name TEXT,
         contact TEXT,
         complaint TEXT
      )
   """)
   connection.commit()
   connection.close()

def save_complaint(data):
   connection = sqlite3.connect(DB_PATH)
   cursor = connection.cursor()
   cursor.execute("""
      INSERT INTO complaints (name, contact, complaint) 
      VALUES (?, ?, ?)
   """, (data['name'], data['contact'], data['complaint']))
   connection.commit()
   connection.close()
