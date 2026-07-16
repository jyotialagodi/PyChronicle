import sqlite3

DB_NAME = "pychronicle.db"

connection = sqlite3.connect(DB_NAME)
cursor = connection.cursor()

cursor.execute("""
SELECT line_number,
       variable_name,
       serialized_value
FROM variable_states
ORDER BY line_number,id
""")

records = cursor.fetchall()

print("=" * 60)
print("        PYCHRONICLE EXECUTION TIMELINE")
print("=" * 60)

current_line = None

for line, variable, value in records:

    if current_line != line:
        current_line = line
        print()
        print(f"Line {line}")
        print("-" * 25)

    print(f"{variable} = {value}")

connection.close()