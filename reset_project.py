import sqlite3
import os

DATABASE_NAME = "pychronicle.db"

try:
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("DELETE FROM variable_states")

    connection.commit()
    connection.close()

    if os.path.exists("execution_report.txt"):
        os.remove("execution_report.txt")

    print("===================================")
    print("PyChronicle Reset Completed")
    print("===================================")
    print("Database Cleared")
    print("Execution Report Deleted")
    print("Project Ready For New Execution")

except Exception as e:
    print(e)