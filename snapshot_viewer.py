import sqlite3

DB_NAME = "pychronicle.db"

connection = sqlite3.connect(DB_NAME)
cursor = connection.cursor()

line_number = int(input("Enter line number: "))

cursor.execute("""
SELECT variable_name, serialized_value
FROM variable_states
WHERE line_number = ?
ORDER BY variable_name
""", (line_number,))

records = cursor.fetchall()

print("\n" + "=" * 40)
print(f"Variables at Line {line_number}")
print("=" * 40)

if records:
    for variable_name, value in records:
        print(f"{variable_name} = {value}")
else:
    print("No variables found for this line.")

connection.close()