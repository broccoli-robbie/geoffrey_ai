import os
from config import MAX_CHARS


def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        abs_working_directory: str = os.path.abspath(working_directory)
        abs_target: str = os.path.abspath(
            os.path.join(abs_working_directory, file_path)
        )

        if not abs_target.startswith(abs_working_directory):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(abs_target):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(abs_target, "r") as f:
            content: str = f.read(MAX_CHARS)
            if f.read(1):
                content += f'...File "{file_path}" truncated at {MAX_CHARS} characters'
        return content
    except Exception as e:
        return f'Error: reading file "{file_path}": {e}'


schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": f"Retrieves the content (at most {MAX_CHARS} characters) of a specified file within the working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to read, relative to the working directory",
                },
            },
            "required": ["file_path"],
        },
    },
}
