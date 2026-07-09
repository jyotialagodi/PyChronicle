import sqlite3

connection = sqlite3.connect("pychronicle.db")
cursor = connection.cursor()

cursor.execute("""
SELECT id, timestamp, line_number, variable_name, serialized_value
FROM variable_states
ORDER BY id
""")

records = cursor.fetchall()

print("Saved variable states:")
print("-" * 60)

for record in records:
    print(record)

print("-" * 60)
print(f"Total records: {len(records)}")

connection.close()