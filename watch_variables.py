import sqlite3

DATABASE_NAME = "pychronicle.db"

connection = sqlite3.connect(DATABASE_NAME)
cursor = connection.cursor()

# Get latest session
cursor.execute("""
SELECT session_id
FROM variable_states
ORDER BY id DESC
LIMIT 1
""")

session = cursor.fetchone()

if session is None:
    print("No execution history found.")
    exit()

session_id = session[0]

variable = input("Enter Variable Name : ")

cursor.execute("""
SELECT line_number,
       serialized_value
FROM variable_states
WHERE session_id = ?
AND variable_name = ?
ORDER BY id
""", (session_id, variable))

records = cursor.fetchall()

print()
print("=" * 40)
print("WATCH VARIABLE")
print("=" * 40)

if records:

    for line, value in records:

        print(f"Line {line}  --->  {variable} = {value}")

else:

    print("Variable not found.")

connection.close()