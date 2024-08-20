import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="#Fuckshit26", # <--- my bad thought it was private lol
        database="library"
    )


def add_book():
    db = connect_db()
    cursor = db.cursor()

    title = input("Enter book title: ")
    author_id = input("Enter author ID: ")
    isbn = input("Enter ISBN: ")
    publication_date = input("Enter publication date (YYYY-MM-DD): ")

    query = "INSERT INTO books (title, author_id, isbn, publication_date) VALUES (%s, %s, %s, %s)"
    values = (title, author_id, isbn, publication_date)

    cursor.execute(query, values)
    db.commit()

    print("Book added successfully!")
    cursor.close()
    db.close()

def fetch_all_books():
    db = connect_db()
    cursor = db.cursor()

    query = "SELECT * FROM books"
    cursor.execute(query)

    books = cursor.fetchall()
    for book in books:
        print(f"ID: {book[0]}")
        print(f"Title: {book[1]}")
        print(f"Author ID: {book[2]}")
        print(f"ISBN: {book[3]}")
        print(f"Publication Date: {book[4]}")
        print(f"Availability: {'Yes' if book[5] else 'No'}")
        print("----")

    cursor.close()
    db.close()

def borrow_book():
    db = connect_db()
    cursor = db.cursor()

    # Fetch available books
    query = "SELECT * FROM books WHERE availability = 1"
    cursor.execute(query)
    books = cursor.fetchall()

    if not books:
        print("No books are currently available for borrowing.")
        return

    # Display available books
    for book in books:
        print(f"ID: {book[0]}")
        print(f"Title: {book[1]}")
        print(f"Author ID: {book[2]}")
        print(f"ISBN: {book[3]}")
        print(f"Publication Date: {book[4]}")
        print("----")

    # Prompt user to select a book
    book_id = int(input("Enter the ID of the book you want to borrow: "))
    customer_id = int(input("Enter your customer ID: "))
    borrow_date = input("Enter the borrow date (YYYY-MM-DD): ")

    # Update the book's availability
    update_query = "UPDATE books SET availability = 0 WHERE id = %s"
    cursor.execute(update_query, (book_id,))

    # Insert into borrowed_books table
    insert_query = """
    INSERT INTO borrowed_books (customer_id, book_id, borrow_date)
    VALUES (%s, %s, %s)
    """
    cursor.execute(insert_query, (customer_id, book_id, borrow_date))
    db.commit()

    print(f"Book with ID {book_id} has been borrowed successfully.")

    cursor.close()
    db.close()

def return_book():
    db = connect_db()
    cursor = db.cursor()

    # Prompt user to enter the book ID
    book_id = int(input("Enter the ID of the book you want to return: "))
    return_date = input("Enter the return date (YYYY-MM-DD): ")

    # Check if the book is currently borrowed
    query = "SELECT availability FROM books WHERE id = %s"
    cursor.execute(query, (book_id,))
    result = cursor.fetchone()

    if result is None:
        print("Book not found in the library.")
    elif result[0] == 1:
        print("This book is already available in the library.")
    else:
        # Update the book's availability
        update_query = "UPDATE books SET availability = 1 WHERE id = %s"
        cursor.execute(update_query, (book_id,))

        # Update the return date in borrowed_books table
        update_borrowed_query = """
        UPDATE borrowed_books
        SET return_date = %s
        WHERE book_id = %s AND return_date IS NULL
        """
        cursor.execute(update_borrowed_query, (return_date, book_id))
        db.commit()

        print(f"Book with ID {book_id} has been returned successfully.")

    cursor.close()
    db.close()
