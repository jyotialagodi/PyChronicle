import sqlite3
DATABASE_NAME = "pychronicle.db"
connection = sqlite3.connect(DATABASE_NAME)
cursor = connection.cursor()
cursor.execute("""SELECT variable_name,serialized_value,line_number
               FROM variable_states
               ORDER BY variable_name,id""")
records=cursor.fetchall()
connection.close()
print("="*60)
print("PYCHRONICLE CHANGE DETECTOR")
print("="*60)
previous_values={}
for variable_name, value, line in records:
    if variable_name not in previous_values:
        previous_values[variable_name]=value
        print(f"\nVariable:{variable_name}")
        print(f"Initial Value:{value}")
        print(f"Line:{line}")
        print("-"*40)
    else:
        old_value=previous_values[variable_name]
        print(f"\nVariable:{variable_name}")
        print(f"previous:{old_value}")
        print(f"current:{value}")
        print(f"Line:{line}")
        if old_value==value:
            print("Status:UNCHANGED")
        else:
            print("Status:CHANGED")
            print("-"*40)
            previous_values[variable_name]=value

