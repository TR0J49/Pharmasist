import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('sqlite3.db')
cursor = conn.cursor()

try:
    # Create tables if they don't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS Medications (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        type TEXT,
                        dosage TEXT,
                        quantity INTEGER,
                        price REAL
                      )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Healthcare_Products (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        category TEXT,
                        quantity INTEGER,
                        price REAL
                      )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Customers (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        email TEXT,
                        phone TEXT,
                        address TEXT,
                        medicine TEXT,
                        quantity TEXT,
                        price TEXT
                      )''')

    # Insert sample data into Medications table
    medications_additional_data = [
        # Add your medication data here
    ]

    cursor.executemany('''INSERT INTO Medications (name, type, dosage, quantity, price)
                          VALUES (?, ?, ?, ?, ?)''', medications_additional_data)

    # Insert sample data into Healthcare_Products table
    healthcare_products_additional_data = [
        # Add your healthcare product data here
    ]

    cursor.executemany('''INSERT INTO Healthcare_Products (name, category, quantity, price)
                          VALUES (?, ?, ?, ?)''', healthcare_products_additional_data)

    # Prompt the user for customer information
    name = input("Enter customer name: ")
    email = input("Enter customer email: ")
    phone = input("Enter customer phone number: ")
    address = input("Enter customer address: ")
    medicine = input("Enter medicine name: ")
    quantity = int(input("Enter quantity: "))  # Ensure quantity is converted to int
    price = float(input("Enter price: "))  # Ensure price is converted to float

    # Insert customer data into Customers table
    cursor.execute('''INSERT INTO Customers (name, email, phone, address, medicine, quantity, price)
                      VALUES (?, ?, ?, ?, ?, ?, ?)''', (name, email, phone, address, medicine, quantity, price))

    # Update quantity of purchased item in Medications or Healthcare_Products table
    cursor.execute('''UPDATE Medications SET quantity = quantity - ? WHERE name = ?''', (quantity, medicine))
    # For Healthcare_Products table, change the table name accordingly if needed
    # Update quantity of purchased item in Healthcare_Products table
    cursor.execute('''UPDATE Healthcare_Products SET quantity = quantity - ? WHERE name = ?''', (quantity, medicine))

    # Commit changes to the database
    conn.commit()
    print("Data inserted successfully!")

except sqlite3.Error as e:
    print("SQLite error:", e)

finally:
    # Close the database connection
    conn.close()
