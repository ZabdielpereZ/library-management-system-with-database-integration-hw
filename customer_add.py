from db_connection import connect_db, Error
import random, string

def generate_libarary_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k =  10))
library_id = generate_libarary_id()


def add_customer():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            name = input("what is your name? ").title()
            email = input("what is your email? ").title()
            phone = input("what is your phone number? ")
            library_id = generate_libarary_id()

            new_customer = (name, email, phone, library_id)

            query = "INSERT INTO customer (customer_name, email, phone, library_id) VALUES (%s, %s, %s, %s)"

            cursor.execute(query, new_customer)
            conn.commit() # fully commits the changes wwe are trying to make (adding data to the customer table)
            print(f"New customer {name} added successfully")

        except Error as e:
            print(f"Error: {e}")

        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close() #ALWAYS

def update_customer_email():
    conn = connect_db()

    if conn is not None:
        try:
            cursor = conn.cursor()

            customer_id = input("What is the ID of the customer you'd like to update? ")
            email = input("What is the new email? ")

            email_update = (email, customer_id)

            query = "UPDATE customer SET email = %s WHERE id = %s"

            cursor.execute(query, email_update)
            conn.commit()
            print("Successfully updated customer phone number!")

        except Error as e:
            print(f"Error: {e}")

        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

def update_customer_name():
    conn = connect_db()

    if conn is not None:
        try:
            cursor = conn.cursor()

            customer_id = input("What is the ID of the customer you'd like to update? ")
            name = input("What is the new name? ")

            name_update = (name, customer_id)

            query = "UPDATE customer SET name = %s WHERE id = %s"

            cursor.execute(query, name_update)
            conn.commit()
            print("Successfully updated customer phone number!")

        except Error as e:
            print(f"Error: {e}")

        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()


if __name__ == "__main__":
    add_customer()
