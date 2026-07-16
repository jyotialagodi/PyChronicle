import sqlite3
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

DB_NAME = "pychronicle.db"

connection = sqlite3.connect(DB_NAME)
cursor = connection.cursor()

cursor.execute("""
SELECT line_number, variable_name, serialized_value
FROM variable_states
ORDER BY line_number, id
""")

records = cursor.fetchall()

root = tk.Tk()
root.title("Execution Timeline")
root.geometry("700x500")

title = tk.Label(
    root,
    text="Execution Timeline",
    font=("Arial", 16, "bold")
)
title.pack(pady=10)

text = ScrolledText(root, width=80, height=25)
text.pack(padx=10, pady=10, fill="both", expand=True)

current_line = None

for line, variable, value in records:

    if current_line != line:
        current_line = line
        text.insert(tk.END, "\n")
        text.insert(tk.END, "=" * 50 + "\n")
        text.insert(tk.END, f"Line {line}\n")
        text.insert(tk.END, "=" * 50 + "\n")

    text.insert(tk.END, f"{variable} = {value}\n")

text.config(state="disabled")

connection.close()

root.mainloop()