import sqlite3

DB_NAME = "pychronicle.db"

# Connect to SQLite Database
connection = sqlite3.connect(DB_NAME)
cursor = connection.cursor()

# --------------------------------------
# Total Records
# --------------------------------------
cursor.execute("""
SELECT COUNT(*)
FROM variable_states
""")

total_records = cursor.fetchone()[0]

# --------------------------------------
# Unique Variables
# --------------------------------------
cursor.execute("""
SELECT COUNT(DISTINCT variable_name)
FROM variable_states
""")

unique_variables = cursor.fetchone()[0]

# --------------------------------------
# Unique Lines Executed
# --------------------------------------
cursor.execute("""
SELECT COUNT(DISTINCT line_number)
FROM variable_states
""")

unique_lines = cursor.fetchone()[0]

# --------------------------------------
# Display Statistics
# --------------------------------------

print("=" * 50)
print("           PYCHRONICLE STATISTICS")
print("=" * 50)

print(f"Total Records          : {total_records}")
print(f"Unique Variables       : {unique_variables}")
print(f"Unique Lines Executed  : {unique_lines}")

print("=" * 50)

connection.close()