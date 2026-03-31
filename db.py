import sqlite3
from datetime import datetime
#CONSTANT name for the database file
DB_NAME = 'moneywatch.db'

def init_db():
    #connect to the database 
    conn = sqlite3.connect(DB_NAME) 
   
    #create a cursor object to execute SQL commands
    cursor = conn.cursor()

    #execute sql commands to create the transactions table if it doesn't exist
    cursor.execute("""CREATE TABLE IF NOT EXISTS transactions (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   amount REAL NOT NULL, 
                   category TEXT NOT NULL, 
                   description TEXT,
                   type TEXT CHECK(type IN ('income', 'expense')) NOT NULL,
                   date TEXT DEFAULT CURRENT_DATE)""")
    
    #commit the changes and close the connection
    conn.commit()
    conn.close()
                                    
#write a function to add a transaction to the database
#add_transaction 
def add_transaction(amount,category,description,type):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute



