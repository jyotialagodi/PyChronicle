import sys
import os
from datetime import datetime

from database import create_database, save_variable_state


TARGET_FILE = os.path.abspath("target_program.py")

# Stores the previous value of each variable
previous_variables = {}


def trace_execution(frame, event, arg):
    current_file = os.path.abspath(frame.f_code.co_filename)

    # Trace only target_program.py
    if current_file != TARGET_FILE:
        return trace_execution

    if event == "line":
        line_number = frame.f_lineno
        local_variables = frame.f_locals.copy()

        # Remove unwanted Python built-in data
        local_variables.pop("__builtins__", None)

        # Check every current variable
        for variable_name, variable_value in local_variables.items():

            serialized_value = repr(variable_value)

            # Save only if variable is new or its value changed
            if (
                variable_name not in previous_variables
                or previous_variables[variable_name] != serialized_value
            ):
                print(
                    f"CHANGE → Line {line_number} | "
                    f"{variable_name} = {serialized_value}"
                )

                save_variable_state(
                    datetime.now().isoformat(),
                    line_number,
                    variable_name,
                    serialized_value
                )

                # Remember the latest value
                previous_variables[variable_name] = serialized_value

    return trace_execution


# Make sure database and table exist
create_database()


# Read target_program.py
with open("target_program.py", "r") as file:
    source_code = file.read()


# Compile target program
compiled_code = compile(
    source_code,
    TARGET_FILE,
    "exec"
)


# Clean execution environment
clean_environment = {
    "__builtins__": __builtins__
}


# Start tracing
sys.settrace(trace_execution)

# Run target_program.py
exec(compiled_code, clean_environment)

# Stop tracing
sys.settrace(None)