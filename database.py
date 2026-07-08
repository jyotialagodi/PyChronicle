import sqlite3
from datetime import datetime


connection = sqlite3.connect("pychronicle.db")
cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS variable_states (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT NOT NULL,
    line_number INTEGER NOT NULL,
    variable_name TEXT NOT NULL,
    serialized_value TEXT
)
""")


cursor.execute("""
INSERT INTO variable_states
(timestamp, line_number, variable_name, serialized_value)
VALUES (?, ?, ?, ?)
""", (
    datetime.now().isoformat(),
    1,
    "x",
    "10"
))


connection.commit()


cursor.execute("SELECT * FROM variable_states")

records = cursor.fetchall()

print("Stored variable states:")

for record in records:
    print(record)


connection.close()