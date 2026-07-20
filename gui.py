import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import subprocess


# -----------------------------
# Functions
# -----------------------------

def run_program():
    try:
        subprocess.Popen(["python", "tracer.py"])
    except Exception as e:
        messagebox.showerror("Error", str(e))


def open_timeline():
    try:
        subprocess.Popen(["python", "timeline_viewer.py"])
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
    except Exception as e:
        messagebox.showerror("Error", str(e))


def open_summary():
    try:
        subprocess.Popen(["python", "summary_viewer.py"])
    except Exception as e:
        messagebox.showerror("Error", str(e))


# -----------------------------
# NEW FUNCTION
# -----------------------------
def export_report():
    try:
        subprocess.Popen(["python", "export_report.py"])
        messagebox.showinfo(
            "Success",
            "Execution report exported successfully!"
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
# GUI
# -----------------------------

root = tk.Tk()
# -----------------------------
# Menu Bar
# -----------------------------
menu_bar = tk.Menu(root)

root.config(menu=menu_bar)
# -----------------------------
# File Menu
# -----------------------------
file_menu = tk.Menu(menu_bar, tearoff=0)

menu_bar.add_cascade(
    label="File",
    menu=file_menu
)

file_menu.add_command(
    label="Run Program",
    command=run_program
)

file_menu.add_separator()

file_menu.add_command(
    label="Exit",
    command=root.destroy
)
# -----------------------------
# View Menu
# -----------------------------
view_menu = tk.Menu(menu_bar, tearoff=0)

menu_bar.add_cascade(
    label="View",
    menu=view_menu
)

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
# -----------------------------
# Reports Menu
# -----------------------------
report_menu = tk.Menu(menu_bar, tearoff=0)

menu_bar.add_cascade(
    label="Reports",
    menu=report_menu
)

report_menu.add_command(
    label="Export Report",
    command=export_report
)
# -----------------------------
# Help Menu
# -----------------------------
help_menu = tk.Menu(menu_bar, tearoff=0)

menu_bar.add_cascade(
    label="Help",
    menu=help_menu
)

help_menu.add_command(
    label="About",
    command=about
)

root.title("PyChronicle")
root.geometry("550x650")
root.resizable(False, False)

title = tk.Label(
    root,
    text="PyChronicle\nPython Execution Visualizer",
    font=("Arial", 20, "bold")
)

title.pack(pady=20)

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

# -----------------------------
# NEW BUTTON
# -----------------------------
tk.Button(
    root,
    text="Export Report",
    width=30,
    height=2,
    command=export_report
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

root.mainloop()