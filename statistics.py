import sqlite3

DB_NAME = "pychronicle.db"

# Connect to SQLite database
connection = sqlite3.connect(DB_NAME)
cursor = connection.cursor()

# -----------------------------
# Total Records
# -----------------------------
cursor.execute("""
SELECT COUNT(*)
FROM variable_states
""")

total_records = cursor.fetchone()[0]

# -----------------------------
# Unique Variables
# -----------------------------
cursor.execute("""
SELECT COUNT(DISTINCT variable_name)
FROM variable_states
""")

unique_variables = cursor.fetchone()[0]

# -----------------------------
# Display Statistics
# -----------------------------
print("=" * 45)
print("        PYCHRONICLE STATISTICS")
print("=" * 45)

print(f"Total Records      : {total_records}")
print(f"Unique Variables   : {unique_variables}")

print("=" * 45)

# Close database connection
connection.close()