import sqlite3

DB_NAME = "pychronicle.db"

connection = sqlite3.connect(DB_NAME)
cursor = connection.cursor()

cursor.execute("""
SELECT line_number, variable_name, serialized_value
FROM variable_states
ORDER BY line_number, id
""")

records = cursor.fetchall()

print("=" * 50)
print("          EXECUTION TIMELINE")
print("=" * 50)

current_line = None

for line_number, variable_name, value in records:

    if current_line != line_number:
        current_line = line_number
        print(f"\nLine {line_number}")
        print("-" * 25)

    print(f"{variable_name} = {value}")

print("\n" + "=" * 50)
print("End of Timeline")
print("=" * 50)

connection.close()