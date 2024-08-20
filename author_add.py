from db_connection import connect_db

def add_author():
    db = connect_db()
    cursor = db.cursor()

    name = input("Enter the author's name: ")
    birthdate = input("Enter the author's biography: ")

    query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
    cursor.execute(query, (name, birthdate))
    db.commit()

    print(f"Author '{name}' has been added successfully.")

    cursor.close()
    db.close()

def view_author_details():
    db = connect_db()
    cursor = db.cursor()

    author_id = int(input("Enter the author ID: "))

    query = "SELECT * FROM authors WHERE id = %s"
    cursor.execute(query, (author_id,))
    author = cursor.fetchone()

    if author:
        print(f"ID: {author[0]}")
        print(f"Name: {author[1]}")
        print(f"Biography: {author[2]}")
    else:
        print("Author not found.")

    cursor.close()
    db.close()

def display_all_authors():
    db = connect_db()
    cursor = db.cursor()

    query = "SELECT * FROM authors"
    cursor.execute(query)
    authors = cursor.fetchall()

    for author in authors:
        print(f"ID: {author[0]}")
        print(f"Name: {author[1]}")
        print(f"Biography: {author[2]}")
        print("----")

    cursor.close()
    db.close()
