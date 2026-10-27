import os
import subprocess


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        abs_working_directory: str = os.path.abspath(working_directory)
        abs_target: str = os.path.abspath(os.path.join(working_directory, file_path))

        if not abs_target.startswith(abs_working_directory):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(abs_target):
            return f'Error: "{file_path}" does not exist or is not a regular file.'

        if not abs_target.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'

        command: list[str] = ["python", abs_target]
        if args:
            command.extend(args)
        run = subprocess.run(
            command,
            timeout=30,
            capture_output=True,
            cwd=abs_working_directory,
            check=True,
            text=True,
        )
        output: list[str] = []
        if run.returncode != 0:
            output.append(
                f'STDOUT: "{run.stdout}", STDERR: "{run.stderr}", Process exited with code {run.returncode}'
            )
        if not run.stdout and not run.stderr:
            output.append("No output produced")
        if run.stdout:
            output.append(f"STDOUT:\n{run.stdout}")
        if run.stderr:
            output.append(f"STDERR:\n{run.stderr}")
        return "\n".join(output)
    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes a specified Python file within the working directory and returns its output",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the Python file to run, relative to the working directory",
                },
                "args": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Optional list of arguments to pass to the Python script",
                },
            },
            "required": ["file_path"],
        },
    },
}
