import sqlite3
import tkinter as tk

DATABASE_NAME = "pychronicle.db"

connection = sqlite3.connect(DATABASE_NAME)
cursor = connection.cursor()

# Latest session
cursor.execute("""
SELECT session_id
FROM variable_states
ORDER BY id DESC
LIMIT 1
""")

result = cursor.fetchone()

if result is None:
    print("No execution history found.")
    exit()

session_id = result[0]

# Total records
cursor.execute("""
SELECT COUNT(*)
FROM variable_states
WHERE session_id = ?
""", (session_id,))
total_records = cursor.fetchone()[0]

# Unique variables
cursor.execute("""
SELECT COUNT(DISTINCT variable_name)
FROM variable_states
WHERE session_id = ?
""", (session_id,))
variables = cursor.fetchone()[0]

# Unique lines
cursor.execute("""
SELECT COUNT(DISTINCT line_number)
FROM variable_states
WHERE session_id = ?
""", (session_id,))
lines = cursor.fetchone()[0]

connection.close()

root = tk.Tk()
root.title("Execution Summary")
root.geometry("400x250")

tk.Label(
    root,
    text="PYCHRONICLE SUMMARY",
    font=("Arial", 16, "bold")
).pack(pady=15)

tk.Label(root, text=f"Session ID : {session_id}", font=("Arial", 11)).pack(pady=5)
tk.Label(root, text=f"Total Records : {total_records}", font=("Arial", 11)).pack(pady=5)
tk.Label(root, text=f"Variables Tracked : {variables}", font=("Arial", 11)).pack(pady=5)
tk.Label(root, text=f"Lines Executed : {lines}", font=("Arial", 11)).pack(pady=5)

root.mainloop()