import sqlite3

DB_NAME = "pychronicle.db"

variable_name = input("Enter variable name: ")

connection = sqlite3.connect(DB_NAME)
cursor = connection.cursor()

cursor.execute(
    """
    SELECT timestamp, line_number, variable_name, serialized_value
    FROM variable_states
    WHERE variable_name = ?
    ORDER BY id
    """,
    (variable_name,)
)

records = cursor.fetchall()

print(f"\nHistory of variable: {variable_name}")
print("-" * 50)

if records:
    for record in records:
        timestamp, line_number, name, value = record

        print(f"Time  : {timestamp}")
        print(f"Line  : {line_number}")
        print(f"Value : {value}")
        print("-" * 50)
else:
    print("No history found for this variable.")

connection.close()