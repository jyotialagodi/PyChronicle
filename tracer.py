import sys
import os
from datetime import datetime

from database import create_database, save_variable_state

TARGET_FILE = os.path.abspath("target_program.py")

# Create unique session id
SESSION_ID = datetime.now().strftime("%Y%m%d%H%M%S")

# Stores previous values
previous_variables = {}


def trace_execution(frame, event, arg):

    current_file = os.path.abspath(frame.f_code.co_filename)

    if current_file != TARGET_FILE:
        return trace_execution

    if event == "line":

        line_number = frame.f_lineno

        local_variables = frame.f_locals.copy()

        local_variables.pop("__builtins__", None)

        for variable_name, variable_value in local_variables.items():

            serialized_value = repr(variable_value)

            if (
                variable_name not in previous_variables
                or previous_variables[variable_name] != serialized_value
            ):

                print(
                    f"[{SESSION_ID}] "
                    f"Line {line_number} "
                    f"{variable_name} = {serialized_value}"
                )

                save_variable_state(
                    SESSION_ID,
                    datetime.now().isoformat(),
                    line_number,
                    variable_name,
                    serialized_value
                )

                previous_variables[variable_name] = serialized_value

    return trace_execution


create_database()

with open("target_program.py", "r") as file:
    source_code = file.read()

compiled_code = compile(
    source_code,
    TARGET_FILE,
    "exec"
)

clean_environment = {
    "__builtins__": __builtins__
}

sys.settrace(trace_execution)

exec(compiled_code, clean_environment)

sys.settrace(None)

print("\nExecution Completed.")
print("Session ID :", SESSION_ID)