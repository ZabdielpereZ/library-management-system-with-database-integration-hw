import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="#Fuckshit26", # <--- my bad thought it was private lol
        database="library"
    )

def fetch_book():
    db = connect_db()
    cursor = db.cursor()

    book_id = input("Enter book ID: ")

    query = "SELECT * FROM books WHERE id = %s"
    cursor.execute(query, (book_id,))

    book = cursor.fetchone()
    if book:
        print(f"ID: {book[0]}")
        print(f"Title: {book[1]}")
        print(f"Author ID: {book[2]}")
        print(f"ISBN: {book[3]}")
        print(f"Publication Date: {book[4]}")
        print(f"Availability: {'Yes' if book[5] else 'No'}")
    else:
        print("Book not found.")

    cursor.close()
    db.close()
