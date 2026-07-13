def open_snapshot():
    import tkinter as tk
    from tkinter import simpledialog

    line = simpledialog.askinteger(
        "Snapshot Viewer",
        "Enter Line Number:"
    )

    if line is None:
        return

    try:
        subprocess.run(
            ["python", "snapshot_viewer.py", str(line)],
            check=True
        )
    except Exception as e:
        messagebox.showerror("Error", str(e))