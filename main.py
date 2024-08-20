from book_add import add_book, fetch_all_books, borrow_book, return_book
from book_fetch import fetch_book
from customer_add import add_customer
from customer_fetch import fetch_all_customers, fetch_customer
from author_add import add_author, view_author_details, display_all_authors
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def customer_menu():
    clear()
    while True:
        action = input('''
Customer Menu:
1 - Add Customer
2 - View Customer Details
3 - Display All Customers
4 - Main Menu
5 - Clear Terminal
''')
        
        if action == '1':
            add_customer()
        elif action == '2':
            fetch_customer() # view specific customer
        elif action == '3':
            fetch_all_customers() # display all customers
        elif action == '4':
            break
        elif action == '5':
            clear()

def book_menu():
    clear()
    while True:
        action = input('''
Book Menu:
1 - Add Book
2 - View Book Details
3 - Display All Books
4 - Main Menu
5 - Clear Terminal
6 - Borrow Book
7 - Return Book
Enter your choice: ''')
        
        if action == '1':
            clear()
            add_book()
        elif action == '2':
            clear()
            fetch_book() # view specific book
        elif action == '3':
            clear()
            fetch_all_books() # display all books
        elif action == '4':
            break
        elif action == '5':
            clear()
        elif action == '6':
            clear()
            borrow_book()
        elif action == '7':
            return_book()
        else:
            print("Invalid choice. Please try again.")

def author_menu():
    while True:
        print("Author Operations:")
        print("1 - Add a new author")
        print("2 - View author details")
        print("3 - Display all authors")
        print("4 - Main Menu")
        print("5 - Clear Terminal")
        action = int(input("Enter your choice: "))

        if action == 1:
            clear()
            add_author()
        elif action == 2:
            clear()
            view_author_details()
        elif action == 3:
            clear()
            display_all_authors()
        elif action == 4:
            break
        elif action == 5:
            clear()
        else:
            print("Invalid choice. Please try again.")


while True:

    action = input('''
Main Menu:
1 - Customer Actions
2 - Book Actions
3 - Author Actions
4 - Quit
''')
    
    if action == '1':
        customer_menu() # customer action stuff
    elif action == '2':
        book_menu() # book action stuff
    elif action == '3':
        clear()
        author_menu() # author action stuff
    elif action == '4':
        clear()
        break
    else:
        print("Pick a number fool!")


