import sqlite3

connection = sqlite3.connect('dp_customers.db')

cursor = connection.cursor()

    

def view_all_customers():
    rows = cursor.execute("SELECT customer_id, name, city, state, phone, email FROM Customers").fetchall()
    print(f'{"Customer ID":<12} {"Name":<23} {"City":<18} {"State":<5} {"Phone":<10} {"Email"}')

    for row in rows:
            print(f'{row[0]:<12} {row[1]:<23} {row[2]:<18} {row[3]:<5} {row[4]} {row[5]}')


def view_single_customer():   
    customer_id_input = input("\nEnter a Customer ID to View a Customer:\n(Press 'Enter' to return to the main menu)\n-----------------------------------------\n\n").lower()
        
    if customer_id_input == "":
        print("\nReturning to the main menu...\n")
        return False

    if customer_id_input.isdigit():
        customer_id = int(customer_id_input)

        row = cursor.execute("SELECT customer_id, name, street_address, city, state, postal_code, phone, email FROM Customers WHERE customer_id=?", (customer_id,)).fetchone()
            
        if row:
            print("\n+++ Customer Details +++\n------------------")
            print(f"Customer ID:      {row[0] if row[0] is not None else 'N/A'}")
            print(f"Name:             {row[1] if row[1] is not None else 'N/A'}")
            print(f"Address:          {row[2] if row[2] is not None else 'N/A'}")
            print(f"City:             {row[3] if row[3] is not None else 'N/A'}")
            print(f"State:            {row[4] if row[4] is not None else 'N/A'}")
            print(f"Zip Code:         {row[5] if row[5] is not None else 'N/A'}")
            print(f"Phone:            {row[6] if row[6] is not None else 'N/A'}")
            print(f"Email:            {row[7] if row[7] is not None else 'N/A'}")
        else:
            print("\nCustomer not found.")
    else:
        print("\nInvalid Customer ID.\n")
    return True
    


def update_or_delete_single_customer():
    customer_id = input("\nTo update or delete a customer, re-enter the customer ID or enter a different customer id or press 'Enter' to go back to the main menu:\n\n ").strip()
    if customer_id == "":
        print("\nReturning to the main menu...\n")
        return 
    elif not customer_id.isdigit():
        print("\nInvalid customer ID. Please enter a valid ID.")
        return
    
    customer_detail_input = input('''
\nTo update a field, enter the first letter of the field.\n
To delete this record, type 'DELETE'.\n
To return to the main menu, press 'Enter'.\n
''').lower()
    if customer_detail_input not in ["n", "a", "c", "s", "z", "p", "e", "delete", ""]:
        print("\nInvalid entry. Please enter n, a, c, s, z, p, e, delete, or enter\n")
        return
    elif customer_detail_input == "":
        print("\nReturning to the main menu...\n")
        return
    elif customer_detail_input == "delete":
        cursor.execute("DELETE FROM Customers WHERE customer_id = ? ", (customer_id,))
        connection.commit()
    elif customer_detail_input == "n":
        new_name = input("\n\nEnter the new name for the customer you'd like to update:\n\n")
        cursor.execute("UPDATE Customers SET name = ? WHERE customer_id = ?",(new_name, customer_id))
        connection.commit()
    elif customer_detail_input == "a":
        new_address = input("\n\nEnter the new address for the customer you'd like to update:\n\n")
        cursor.execute("UPDATE Customers SET street_address = ? WHERE customer_id = ?",(new_address, customer_id))
        connection.commit()
    elif customer_detail_input == "c":
        new_city = input("\n\nEnter the new city for the customer you'd like to update:\n\n")
        cursor.execute("UPDATE Customers SET city = ? WHERE customer_id = ?",(new_city, customer_id))
        connection.commit()
    elif customer_detail_input == "s":
        new_state = input("\n\nEnter the new state for the customer you'd like to update:\n\n")
        cursor.execute("UPDATE Customers SET state = ? WHERE customer_id = ?",(new_state, customer_id))
        connection.commit()
    elif customer_detail_input == "z":
        new_zip = input("\n\nEnter the new zip code for the customer you'd like to update:\n\n")
        cursor.execute("UPDATE Customers SET postal_code = ? WHERE customer_id = ?",(new_zip, customer_id))
        connection.commit()
    elif customer_detail_input == "p":
        new_phone = input("\n\nEnter the new phone number for the customer you'd like to update:\n\n")
        cursor.execute("UPDATE Customers SET phone = ? WHERE customer_id = ?",(new_phone, customer_id))
        connection.commit()
    elif customer_detail_input == "e":
        new_email = input("\n\nEnter the new email for the customer you'd like to update:\n\n")
        cursor.execute("UPDATE Customers SET email = ? WHERE customer_id = ?",(new_email, customer_id))
        connection.commit()


def search_customer():
    customer_name_input = input("\nEnter a Customer name to View a Customer:\n(Press 'Enter' to return to the main menu)\n-----------------------------------------\n\n").strip().lower()

    if customer_name_input == "":
        print("\nReturning to the main menu...\n")
        return
    else:
        print(f"Searching for customer: '{customer_name_input}'")

        result = cursor.execute("SELECT customer_id, name, city, state, phone, email FROM Customers WHERE name LIKE ?", ("%"+customer_name_input+"%",)).fetchall()
        

        if result:
            print("\n+++ Customer Details +++\n------------------")
            print(f'{"Customer ID":<12} {"Name":<23} {"City":<18} {"State":<5} {"Phone":<10} {"Email"}')

            for row in result:
                print(f'{row[0]:<12} {row[1]:<23} {row[2]:<18} {row[3]:<5} {row[4]} {row[5]}')
        else:
            print("\nCustomer details not found.")


def add_new_customer():
    input("\nPlease fill out the form below to add a new Customer:\n(Press 'Enter' to begin)\n-----------------------------------------\n\n")
    
    customer_name = input("Name     :")
    customer_address = input("Address  :")
    customer_city = input("City     :")
    customer_state = input("State    :")
    customer_zip = input("Zip Code :")
    customer_phone = input("Phone    :")
    customer_email = input("Email    :")
    
    insert_sql = "INSERT INTO Customers (name, street_address, city, state, postal_code, phone, email) VALUES (?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(insert_sql, (customer_name, customer_address, customer_city, customer_state, customer_zip, customer_phone, customer_email))
    connection.commit()




print("*** Customer Database ***\n------------------------------------------")
while True:
    person = input("""

[1] View All Customers
[2] Search Cutomers
[3] Add a New Customer
[Q] Quit\n
""").lower()

    
    if person == "1":
        view_all_customers()
        if not view_single_customer():
            continue
        update_or_delete_single_customer()
    elif person == "2":
        search_customer()
    elif person == "3":
        add_new_customer()
    elif person == "q":
        print("\nGoodbye!")
        break
    else:
        print("\nInvalid entry. Please enter 1, 2, 3, or Q\n")
        continue
    

connection.close()