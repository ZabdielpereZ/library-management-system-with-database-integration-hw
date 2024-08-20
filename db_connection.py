import mysql.connector # importing the mysql connector that we just pip installed
from mysql.connector import Error # Importing the mysql Error package to deal with specific errors

# CRUD Operations
# Create
# Retrieve
# Update
# Delete

def connect_db():
    # To establish a connection to our database, we're going to need some parameters first
    db_name = 'library'
    user = 'root' # select the specific database user
    password = '#Fuckshit26' # <--- my bad thought it was private lol
    host = '127.0.0.1' # localhost = 127.0.0.1

    # Establish our connection
    try:
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )

        if conn.is_connected():
            print("Connection to MySQL database successful!")
            return conn
        
    except Error as e:
        print(f"Error: {e}")
        return None