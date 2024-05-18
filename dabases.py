import sqlite3

conn = sqlite3.connect('order_db.db')
conn.execute('PRAGMA foreign_keys =ON')

cursor = conn.cursor()

cursor.execute("Select * from Customers;")

# for customer in cursor:
#     print(customer)


name  = "Alice Brown" 
# cursor.execute("Select * from Customers where CustomerName=?", (name,))
# print(cursor.fetchone())
query ="""
   Select Customers.CustomerName,Customers.CustomerAdress,Orders.OrderId, 
   Products.ProductID,Products.ProductName from Customers 
   INNER JOIN Orders ON Customers.CustomerID = Orders.CustomerId
   INNER JOIN Products ON Orders.ProductId = Products.ProductID 
   WHERE Customers.CustomerName = ?;
   """
cursor.execute(query, (name,))

for record in cursor:
    print(record)