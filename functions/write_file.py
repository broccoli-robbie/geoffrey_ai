import os


def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        abs_working_directory: str = os.path.abspath(working_directory)
        abs_target: str = os.path.abspath(
            os.path.join(abs_working_directory, file_path)
        )
        target_dir: str = os.path.dirname(abs_target)

        if not abs_target.startswith(abs_working_directory):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if os.path.isdir(abs_target):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        os.makedirs(target_dir, exist_ok=True)
        with open(abs_target, "w") as f:
            f.write(content)
        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )
    except Exception as e:
        return f"Error: writing to file: {e}"


schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes text content to a specified file within the working directory (overwriting if the file exists)",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to write, relative to the working directory",
                },
                "content": {
                    "type": "string",
                    "description": "Text content to write to the file",
                },
            },
            "required": ["file_path", "content"],
        },
    },
}
