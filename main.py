import sqlite3


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

    
    
    medications_additional_data = [
        
    ]

    cursor.executemany('''INSERT INTO Medications (name, type, dosage, quantity, price)
                          VALUES (?, ?, ?, ?, ?)''', medications_additional_data)

    
    healthcare_products_additional_data = [
       
    ]

    cursor.executemany('''INSERT INTO Healthcare_Products (name, category, quantity, price)
                          VALUES (?, ?, ?, ?)''', healthcare_products_additional_data)

   
    name = input("Enter customer name: ")
    email = input("Enter customer email: ")
    phone = input("Enter customer phone number: ")
    address = input("Enter customer address: ")
    medicine = input("Enter medicine name: ")
    quantity = int(input("Enter quantity: "))  
    price = float(input("Enter price: "))  

    
    cursor.execute('''INSERT INTO Customers (name, email, phone, address, medicine, quantity, price)
                      VALUES (?, ?, ?, ?, ?, ?, ?)''', (name, email, phone, address, medicine, quantity, price))

   
    cursor.execute('''UPDATE Medications SET quantity = quantity - ? WHERE name = ?''', (quantity, medicine))
   
    cursor.execute('''UPDATE Healthcare_Products SET quantity = quantity - ? WHERE name = ?''', (quantity, medicine))

   

    conn.commit()
    print("Data inserted successfully!")

except sqlite3.Error as e:
    print("SQLite error:", e)

finally:
   
    
    conn.close()
