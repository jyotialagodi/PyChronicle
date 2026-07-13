import tkinter as tk
from tkinter import messagebox
import subprocess

# Function to run tracer.py
def run_program():
    try:
        subprocess.run(["python", "tracer.py"], check=True)
        messagebox.showinfo("Success", "Program executed successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Placeholder functions
def timeline():
    messagebox.showinfo("Timeline", "Timeline Viewer will be connected next.")

def history():
    messagebox.showinfo("History", "Variable History Viewer will be connected next.")

def snapshot():
    messagebox.showinfo("Snapshot", "Snapshot Viewer will be connected next.")

# Main Window
root = tk.Tk()
root.title("PyChronicle")
root.geometry("500x450")
root.resizable(False, False)

title = tk.Label(
    root,
    text="PyChronicle\nPython Execution Visualizer",
    font=("Arial", 18, "bold")
)
title.pack(pady=20)

tk.Button(root, text="Run Program", width=30, height=2,
          command=run_program).pack(pady=8)

tk.Button(root, text="Execution Timeline", width=30, height=2,
          command=timeline).pack(pady=8)

tk.Button(root, text="Variable History", width=30, height=2,
          command=history).pack(pady=8)

tk.Button(root, text="Snapshot Viewer", width=30, height=2,
          command=snapshot).pack(pady=8)

tk.Button(root, text="Exit", width=30, height=2,
          command=root.destroy).pack(pady=20)

root.mainloop()
