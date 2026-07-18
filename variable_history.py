import sqlite3
import sys

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
# Get Variable Name from GUI
# ---------------------------------------
if len(sys.argv) > 1:
    variable_name = sys.argv[1]
else:
    print("Variable name not provided.")
    connection.close()
    exit()

# ---------------------------------------
# Query Variable History
# ---------------------------------------
cursor.execute("""
SELECT timestamp,
       line_number,
       serialized_value
FROM variable_states
WHERE session_id = ?
AND variable_name = ?
ORDER BY id
""", (session_id, variable_name))

records = cursor.fetchall()

print("=" * 60)
print(f"VARIABLE HISTORY : {variable_name}")
print("=" * 60)
print(f"Session ID : {session_id}")
print("=" * 60)

if records:

    for timestamp, line_number, value in records:

        print(f"Time  : {timestamp}")
        print(f"Line  : {line_number}")
        print(f"Value : {value}")
        print("-" * 40)

else:

    print("No history found for this variable.")

connection.close()