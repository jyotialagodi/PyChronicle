import sqlite3

DATABASE_NAME = "pychronicle.db"

connection = sqlite3.connect(DATABASE_NAME)
cursor = connection.cursor()

# ---------------------------------------
# Get Latest Session ID
# ---------------------------------------
cursor.execute("""
SELECT session_id
FROM variable_states
ORDER BY id DESC
LIMIT 1
""")

latest_session = cursor.fetchone()

if latest_session is None:
    print("No execution history found.")
    connection.close()
    exit()

session_id = latest_session[0]

# ---------------------------------------
# Get Timeline for Latest Session
# ---------------------------------------
cursor.execute("""
SELECT line_number,
       variable_name,
       serialized_value
FROM variable_states
WHERE session_id = ?
ORDER BY line_number, id
""", (session_id,))

records = cursor.fetchall()

print("=" * 60)
print("        PYCHRONICLE EXECUTION TIMELINE")
print("=" * 60)
print(f"Session ID : {session_id}")
print("=" * 60)

current_line = None

for line, variable, value in records:

    if current_line != line:
        current_line = line
        print()
        print(f"Line {line}")
        print("-" * 30)

    print(f"{variable} = {value}")

connection.close()