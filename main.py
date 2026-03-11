

import sqlite3

connection = sqlite3.connect('dp_customers.db')

cursor = connection.cursor()


# user_value_1 = input("Enter a field you want from the database: ")
# user_value_2 = input("Enter a field you want from the database: ")

# rows = cursor.execute(f"SELECT {user_value_1}, {user_value_2} FROM Products WHERE make = 'Tenba'").fetchall()
# NEVER use Python string operations to dynamically create an SQL statement. Using String operations leaves 
# you vulnerable to an attack called an SQL Injection Attack, which is where malicious individuals can pass 
# strings to your functions that will close one SQL command and start any number of other commands to be 
# executed on your database. This allows them to steal, modify or delete your data.

# row =cursor.execute("SELECT ?, ? FROM Products", (user_value_1, user_value_2)).fetchall()
# row = cursor.execute(f"SELECT {user_value_1}, {user_value_2} FROM Products").fetchall()

# print(f"{user_value_1:<40}, {user_value_2:<40}")

# for row in row:
#     print(f"{row[0]:<40} {row[1]:<40}")





# EXERCISE
# rows = cursor.execute("SELECT name, city, state, postal_code FROM Customers").fetchall()

# columns = ['name', 'city', 'state', 'postal_code']

# print(f'{"Name":<25} {"City":<25} {"State":<25} {"Postal Code":<25}')

# for row in rows:
#    print(f'{row[0]:<23} {row[1]:<20} {row[2]:<7} {row[3]}')



# EXERCISE
# inser_sql = "INSERT INTO Customers (name, street_address, city, state, postal_code) VALUES (?, ?, ?, ?, ?)"

# values = ("Biff", "365 W Jerk Dr", "Somewhere", "WA", "90210")

# cursor.execute(inser_sql, values)

# connection.commit()



# EXERCISE
# sql_update = "UPDATE Customers SET name=?, street_address=?, postal_code=?, email=?, phone=? WHERE customer_id=?"
# update_values = ('ABCYA Tees', '156 Excitment Way', '90216', 'info@abcyatees.com', '801-108-1808', 56)

# cursor.execute(sql_update, update_values)

# connection.commit()




# EXERCISE
# insert_sql = "INSERT INTO Customers (name, city, state, postal_code) VALUES (?, ?, ?, ?)"

# florida = [
#     ("Harry", "Tampa", "FL", "34110"),
#     ("Ron", "Tampa", "FL", "34110"),
#     ("Hermione", "Tampa", "FL", "34110"),
#     ("Ginny", "Tampa", "FL", "34110"),
#     ("Luna", "Tampa", "FL", "34110")
# ]
# utah = [
#     ("Neville", "Manti", "UT", "84950"),
#     ("Fred", "Manti", "UT", "84950"),
#     ("George", "Manti", "UT", "84950"),
#     ("Dudley", "Manti", "UT", "84950"),
#     ("Petunia", "Manti", "UT", "84950")
# ]

# insert_sql_2 = "INSERT INTO Customers (name, street_address, city, state, postal_code) VALUES (?, ?, ?, ?, ?)"

# texas = [
#     ("Vernon", "12 E 600 S", "Houston", "TX", "79312"),
#     ("Hagrid", "22 E 600 S", "Houston", "TX", "79312"),
#     ("Severus", "32 E 600 S", "Houston", "TX", "79312"),
#     ("Dumbledore", "42 E 600 S", "Houston", "TX", "79312"),
#     ("Voldemort", "52 E 600 S", "Houston", "TX", "79312")
# ]

# cursor.executemany(insert_sql, florida)
# cursor.executemany(insert_sql, utah)
# cursor.executemany(insert_sql_2, texas)

# connection.commit()






# ********************COPY OF ASSIGNMENT CODE BEFORE I PUT IT INTO FUNCTIONS***********************************

# import sqlite3

# connection = sqlite3.connect('dp_customers.db')

# cursor = connection.cursor()


# print("*** Customer Database ***\n------------------------------------------")
# while True:
#     person = input("""

# [1] View All Customers
# [2] Search Cutomers
# [3] Add a New Customer
# [Q] Quit\n
# """).lower()

#     if person not in ["1", "2", "3", "q"]:
#         print("\nInvalid entry. Please enter 1, 2, 3, or Q\n")
#         continue
    

#     elif person == "1":
#         rows = cursor.execute("SELECT customer_id, name, city, state, phone, email FROM Customers").fetchall()
#         print(f'{"Customer ID":<12} {"Name":<23} {"City":<18} {"State":<5} {"Phone":<10} {"Email"}')

#         for row in rows:
#             print(f'{row[0]:<12} {row[1]:<23} {row[2]:<18} {row[3]:<5} {row[4]} {row[5]}')

#         customer_id_input = input("\nEnter a Customer ID to View a Customer:\n(Press 'Enter' to return to the main menu)\n-----------------------------------------\n\n").lower()
        
#         if customer_id_input == "":
#             print("\nReturning to the main menu...\n")
#             continue

#         if customer_id_input.isdigit():
#             customer_id = int(customer_id_input)

#             row = cursor.execute("SELECT customer_id, name, street_address, city, state, postal_code, phone, email FROM Customers WHERE customer_id=?", (customer_id,)).fetchone()
            
#             if row:
#                 print("\n+++ Customer Details +++\n------------------")
#                 print(f"Customer ID:      {row[0] if row[0] is not None else 'N/A'}")
#                 print(f"Name:             {row[1] if row[1] is not None else 'N/A'}")
#                 print(f"Street Address:   {row[2] if row[2] is not None else 'N/A'}")
#                 print(f"City:             {row[3] if row[3] is not None else 'N/A'}")
#                 print(f"State:            {row[4] if row[4] is not None else 'N/A'}")
#                 print(f"Postal Code:      {row[5] if row[5] is not None else 'N/A'}")
#                 print(f"Phone:            {row[6] if row[6] is not None else 'N/A'}")
#                 print(f"Email:            {row[7] if row[7] is not None else 'N/A'}")
#             else:
#                 print("\nCustomer not found.")
#         else:
#             print("\nInvalid Customer ID.\n")

        
#         customer_detail_input = input(
# '''\nTo update a field, enter the first letter of the field.\n
# To delete this record, type 'DELETE'.\n
# To return to the main menu, press 'Enter'.\n'''
# ).lower()
#         if customer_detail_input not in ["n", "a", "c", "s", "z", "p", "e", "delete", ""]:
#             print("\nInvalid entry. Please enter n, a, c, s, z, p, e, delete, or enter\n")
#             continue
#         elif customer_detail_input == "":
#             print("\nReturning to the main menu...\n")
#             continue
#         elif customer_detail_input == "delete":
#             cursor.execute("DELETE FROM Customers WHERE customer_id = ? ", (customer_id,))
#             print("NOTICE ME")
#             connection.commit()
#         elif customer_detail_input == "n":
#             new_name = input("\n\nEnter the name of the customer you'd like to update:\n\n")
#             cursor.execute("UPDATE Customers SET name = ? WHERE customer_id = ?",(new_name, customer_id))
#         elif customer_detail_input == "a":
#             new_address = input("\n\nEnter the street address of the customer you'd like to update:\n\n")
#             cursor.execute("UPDATE Customers SET street_address = ? WHERE customer_id = ?",(new_address, customer_id))
#         elif customer_detail_input == "c":
#             new_city = input("\n\nEnter the city of the customer you'd like to update:\n\n")
#             cursor.execute("UPDATE Customers SET city = ? WHERE customer_id = ?",(new_city, customer_id))
#         elif customer_detail_input == "s":
#             new_state = input("\n\nEnter the state of the customer you'd like to update:\n\n")
#             cursor.execute("UPDATE Customers SET state = ? WHERE customer_id = ?",(new_state, customer_id))
#         elif customer_detail_input == "z":
#             new_zip = input("\n\nEnter the zip code of the customer you'd like to update:\n\n")
#             cursor.execute("UPDATE Customers SET postal_code = ? WHERE customer_id = ?",(new_zip, customer_id))
#         elif customer_detail_input == "p":
#             new_phone = input("\n\nEnter the phone number of the customer you'd like to update:\n\n")
#             cursor.execute("UPDATE Customers SET phone = ? WHERE customer_id = ?",(new_phone, customer_id))
#         elif customer_detail_input == "e":
#             new_email = input("\n\nEnter the email of the customer you'd like to update:\n\n")
#             cursor.execute("UPDATE Customers SET email = ? WHERE customer_id = ?",(new_email, customer_id))



#     elif person == "2":
#         print("Yes")
        


#     elif person == "3":
#         print("Yep")
       


#     elif person == "q":
#             print("\nGoodbye!")
#             break
    

# connection.close()




#  Number 34 on the quiz: This just turns 183 into a binary number.
# def my_func(var, x = 128):
#   my_val = '0'
#   if var >= x:
#     my_val = '1'
#     var -= x
 
#   if x == 1:
#     return my_val
#   return my_val + my_func(var, x // 2)
 
# print(my_func(183))


# Number 45 on the quiz. It's calling the function 3 times.
# def func_a(num):
#   if num % 2 == 0:
#     return num - 1
#   return num + 2

# print(func_a(func_a(func_a(10))))







# **********CHECK_OUT_TIME_ASSIGNMENT****************************
def checkout_time(customers, n):
    # Initialize a list of registers, each starting with time 0
    registers = [0] * n
    
    # Process each customer
    for customer_time in customers:
        # Find the register with the least time
        min_time = registers[0]  # Start with the first register's time
        min_index = 0  # Start with the first register
        
        for i in range(1, n):  # Start checking from the second register onward
            if registers[i] < min_time:
                min_time = registers[i]
                min_index = i
        
        # Add the customer's checkout time to the register with the least time
        registers[min_index] += customer_time
    
    # The total time is the maximum time among all registers
    return max(registers)


print(checkout_time([8, 5, 10, 2, 6, 3, 4], 3))