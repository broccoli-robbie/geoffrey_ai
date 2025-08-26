import os
import subprocess
from google.genai import types


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs python scripts, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The name of a python file in the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.STRING,
                description="The optional arguments passed to the specified python file. If no arguments are provided, then just execute the python file.",
            ),
        },
    ),
)


def run_python_file(working_directory, file_path, args=[]):
    target_path = os.path.join(working_directory, file_path)
    abs_target = os.path.abspath(target_path)
    abs_working_directory = os.path.abspath(working_directory)

    if not abs_target.startswith(abs_working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(abs_target):
        return f'Error: File "{file_path}" not found.'

    if not abs_target.endswith(".py"):
        return f'Error: File "{file_path}" is not a Python file.'

    try:
        command = ["python3", file_path] + args
        run = subprocess.run(
            command,
            timeout=30,
            capture_output=True,
            cwd=abs_working_directory,
            check=True,
            text=True,
        )
        if run.returncode != 0:
            return f'STDOUT: "{run.stdout}", STDERR: "{run.stderr}", Process exited with code {run.returncode}'
        if run.stdout is None:
            return "No output produced"
        return f'STDOUT: "{run.stdout}", STDERR: "{run.stderr}"'
    except Exception as e:
        return f"Error: executing pythong file: {str(e)}"
