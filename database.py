import sqlite3


DATABASE_NAME = "pychronicle.db"


def create_database():
    connection = sqlite3.connect(DATABASE_NAME)
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

    connection.commit()
    connection.close()

    print("Database and table are ready!")


def save_variable_state(timestamp, line_number, variable_name, serialized_value):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO variable_states
    (timestamp, line_number, variable_name, serialized_value)
    VALUES (?, ?, ?, ?)
    """, (
        timestamp,
        line_number,
        variable_name,
        serialized_value
    ))

    connection.commit()
    connection.close()


if __name__ == "__main__":
    create_database()