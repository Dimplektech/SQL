import sqlite3

"""
This script connects to an SQLite database named 'db_manipul', creates a table
called 'python_programming',inserts student data into the table, performs 
updates on the data,and prints the results.

Operations performed:
1. Create the 'python_programming' table if it doesn't exist.
2. Clear existing data in the table.
3. Insert predefined student data.
4. Select and print all records with grades between 60 and 70.
5. Update Carl Davis's grade to 65.
6. Update the grades of all students with an id greater than 55 to 80.
7. Delete Dennis Fredrickson's row.
8. Print all records after the updates.
9. Close the database connection.
"""


# Connect to the database
db = sqlite3.connect("db_manipul")

# Create a cursor object.
cursor = db.cursor()

# Create python_programming table if it doesn't exist.
cursor.execute(
    """CREATE Table if not EXISTS python_programming (
                    id INTEGER PRIMARY KEY,
                    name VARCHAR(50) NOT NULL,
                    grade INTEGER NOT NULL
                    );"""
)
# Commit the Changes.
db.commit()

# Clear the table before inserting new data.
cursor.execute("""DELETE FROM python_programming""")
db.commit()

# Define the Student Data.
stud_data = [
    [55, "Carl Davis", 61],
    [66, "Dennis Fredrickson", 88],
    [77, "Jane Richards", 78],
    [12, "Peyton Sawyer", 45],
    [2, "Lucas Brooke", 99],
]

# Insert Values in python_programming table.
cursor.executemany(
    """INSERT into python_programming(id,name,grade)
                      values (?,?,?)""",
    stud_data,
)

# Commit Insertion of data.
db.commit()

# Select all records with a grade between 60 and 80
cursor.execute(
    """SELECT * from python_programming where grade
                  BETWEEN ? and ?""",
    (60, 70),
)
# Fetch and print the results.
print("\nAll records with a grade between 60 and 80")
rows = cursor.fetchall()
for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Grade: {row[2]}")

# Change Carl Davis’s grade to 65.
cursor.execute(
    """Update  python_programming set grade = ?
                  WHERE name = ?""",
    (65, "Carl Davis"),
)
# Save changes
db.commit()

# Delete Dennis Fredrickson’s row
cursor.execute(
    """DELETE FROM python_programming 
                  where name = ?""",
    ("Dennis Fredrickson",),
)
# Save changes
db.commit()

# Change the grade of all students with an id greater than 55 to a
# grade of 80.
cursor.execute(
    """Update  python_programming set grade = ?
                  WHERE id > ?""",
    (80, 55),
)
# Save changes
db.commit()

# Print all the records after all update.
cursor.execute("""SELECT * from python_programming""")
rows = cursor.fetchall()
print("\nAll Records after updation: ")
for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Grade: {row[2]}")


# Close the database connection.
db.close()
