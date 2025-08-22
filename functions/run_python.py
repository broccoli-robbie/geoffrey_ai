import os
import subprocess


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
