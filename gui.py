import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import subprocess


# -----------------------------
# GUI
# -----------------------------
root = tk.Tk()

root.title("PyChronicle")
root.geometry("550x680")
root.resizable(False, False)

# -----------------------------
# Status Bar
# -----------------------------
status_bar = tk.Label(
    root,
    text="Status : Ready",
    bd=1,
    relief=tk.SUNKEN,
    anchor="w",
    font=("Arial", 10)
)

# -----------------------------
# Functions
# -----------------------------

def run_program():
    try:
        subprocess.Popen(["python", "tracer.py"])
        status_bar.config(text="Status : Program Executed")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def open_timeline():
    try:
        subprocess.Popen(["python", "timeline_viewer.py"])
        status_bar.config(text="Status : Timeline Opened")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def open_history():
    variable = simpledialog.askstring(
        "Variable History",
        "Enter Variable Name:"
    )

    if variable is None:
        return

    try:
        subprocess.Popen(
            ["python", "variable_history.py", variable]
        )
        status_bar.config(text="Status : Variable History Opened")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def open_snapshot():
    line = simpledialog.askinteger(
        "Snapshot Viewer",
        "Enter Line Number:"
    )

    if line is None:
        return

    try:
        subprocess.Popen(
            ["python", "snapshot_viewer.py", str(line)]
        )
        status_bar.config(text="Status : Snapshot Viewer Opened")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def open_summary():
    try:
        subprocess.Popen(["python", "summary_viewer.py"])
        status_bar.config(text="Status : Summary Opened")
    except Exception as e:
        messagebox.showerror("Error", str(e))
def open_statistics():
    try:
        subprocess.Popen(["python", "statistics.py"])
        status_bar.config(text="Status : Statistics Opened")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def export_report():
   
    try:
        subprocess.Popen(["python", "export_report.py"])
        status_bar.config(text="Status : Report Exported")
        messagebox.showinfo(
            "Success",
            "Execution report exported successfully!"
        )
    except Exception as e:
        messagebox.showerror("Error", str(e))
def clear_database():
    import sqlite3

    try:
        connection = sqlite3.connect("pychronicle.db")
        cursor = connection.cursor()

        cursor.execute("DELETE FROM variable_states")

        connection.commit()
        connection.close()

        status_bar.config(text="Status : Database Cleared")

        messagebox.showinfo(
            "Success",
            "Database cleared successfully!"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))


def about():
    messagebox.showinfo(
        "About",
        "PyChronicle\n\n"
        "Python Execution Visualizer\n\n"
        "Version 2.0"
    )


# -----------------------------
# Menu Bar
# -----------------------------
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# File Menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(
    label="Run Program",
    command=run_program
)

file_menu.add_separator()

file_menu.add_command(
    label="Exit",
    command=root.destroy
)

# View Menu
view_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="View", menu=view_menu)

view_menu.add_command(
    label="Execution Timeline",
    command=open_timeline
)

view_menu.add_command(
    label="Variable History",
    command=open_history
)

view_menu.add_command(
    label="Snapshot Viewer",
    command=open_snapshot
)

view_menu.add_command(
    label="Execution Summary",
    command=open_summary
)
view_menu.add_command(
    label="Statistics",
    command=open_statistics
)

# Reports Menu
report_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Reports", menu=report_menu)

report_menu.add_command(
    label="Export Report",
    command=export_report
)

# Help Menu
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)

help_menu.add_command(
    label="About",
    command=about
)

# -----------------------------
# Title
# -----------------------------
title = tk.Label(
    root,
    text="PyChronicle\nPython Execution Visualizer",
    font=("Arial", 20, "bold")
)

title.pack(pady=20)

# -----------------------------
# Buttons
# -----------------------------
tk.Button(
    root,
    text="Run Program",
    width=30,
    height=2,
    command=run_program
).pack(pady=8)

tk.Button(
    root,
    text="Execution Timeline",
    width=30,
    height=2,
    command=open_timeline
).pack(pady=8)

tk.Button(
    root,
    text="Variable History",
    width=30,
    height=2,
    command=open_history
).pack(pady=8)

tk.Button(
    root,
    text="Snapshot Viewer",
    width=30,
    height=2,
    command=open_snapshot
).pack(pady=8)

tk.Button(
    root,
    text="Execution Summary",
    width=30,
    height=2,
    command=open_summary
).pack(pady=8)

tk.Button(
    root,
    text="📊 Statistics",
    width=30,
    height=2,
    bg="#16A085",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    command=open_statistics
).pack(pady=8)

tk.Button(
    root,
    text="Export Report",
    width=30,
    height=2,
    command=export_report
).pack(pady=8)

tk.Button(
    root,
    text="🗑 Clear Database",
    width=30,
    height=2,
    bg="#C0392B",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    command=clear_database
).pack(pady=8)

tk.Button(
    root,
    text="About",
    width=30,
    height=2,
    command=about
).pack(pady=8)

tk.Button(
    root,
    text="Exit",
    width=30,
    height=2,
    command=root.destroy
).pack(pady=20)

# -----------------------------
# Status Bar
# -----------------------------
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

root.mainloop()