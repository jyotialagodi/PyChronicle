import sqlite3
import tkinter as tk

DATABASE_NAME = "pychronicle.db"

connection = sqlite3.connect(DATABASE_NAME)
cursor = connection.cursor()

# -----------------------------
# Latest Session
# -----------------------------
cursor.execute("""
SELECT session_id
FROM variable_states
ORDER BY id DESC
LIMIT 1
""")

latest = cursor.fetchone()

if latest is None:
    print("No execution history found.")
    exit()

session_id = latest[0]

# -----------------------------
# Total Records
# -----------------------------
cursor.execute("""
SELECT COUNT(*)
FROM variable_states
WHERE session_id = ?
""", (session_id,))

total_records = cursor.fetchone()[0]

# -----------------------------
# Unique Variables
# -----------------------------
cursor.execute("""
SELECT COUNT(DISTINCT variable_name)
FROM variable_states
WHERE session_id = ?
""", (session_id,))

variables = cursor.fetchone()[0]

# -----------------------------
# Unique Lines
# -----------------------------
cursor.execute("""
SELECT COUNT(DISTINCT line_number)
FROM variable_states
WHERE session_id = ?
""", (session_id,))

lines = cursor.fetchone()[0]

connection.close()

# -----------------------------
# GUI
# -----------------------------
root = tk.Tk()

root.title("PyChronicle Statistics")
root.geometry("420x300")
root.resizable(False, False)

tk.Label(
    root,
    text="PYCHRONICLE STATISTICS",
    font=("Segoe UI",16,"bold")
).pack(pady=15)

tk.Label(
    root,
    text=f"Session ID : {session_id}",
    font=("Segoe UI",11)
).pack(pady=5)

tk.Label(
    root,
    text=f"Total Records : {total_records}",
    font=("Segoe UI",11)
).pack(pady=5)

tk.Label(
    root,
    text=f"Variables Tracked : {variables}",
    font=("Segoe UI",11)
).pack(pady=5)

tk.Label(
    root,
    text=f"Unique Lines : {lines}",
    font=("Segoe UI",11)
).pack(pady=5)

root.mainloop()