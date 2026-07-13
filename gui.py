import tkinter as tk
from tkinter import messagebox, simpledialog
import subprocess

# -----------------------------
# Functions
# -----------------------------

def run_program():
    try:
        subprocess.Popen(["python", "tracer.py"])
        messagebox.showinfo("Success", "Program started successfully!")
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
        "Enter Variable Name\n\nExamples:\nx\ny\ni\ntotal\nmessage"
    )

    if not variable:
        return

    try:
        subprocess.Popen(["python", "variable_history.py", variable])
    except Exception as e:
        messagebox.showerror("Error", str(e))


def open_snapshot():
    line = simpledialog.askinteger(
        "Snapshot Viewer",
        "Enter Line Number"
    )

    if line is None:
        return

    try:
        subprocess.Popen(["python", "snapshot_viewer.py", str(line)])
    except Exception as e:
        messagebox.showerror("Error", str(e))


def about():
    messagebox.showinfo(
        "About",
        "PyChronicle\n\nPython Execution Visualizer\nVersion 1.0"
    )


# -----------------------------
# GUI
# -----------------------------

root = tk.Tk()
root.title("PyChronicle")
root.geometry("500x500")
root.resizable(False, False)

title = tk.Label(
    root,
    text="PyChronicle\nPython Execution Visualizer",
    font=("Arial", 18, "bold")
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