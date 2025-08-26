import os
from config import MAX_CHARS
from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Lists the contents of the specified file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The name of a file in the working directory. The contents of this file are to be printed.",
            ),
        },
    ),
)


def get_file_content(working_directory, file_path):
    target_path = os.path.join(working_directory, file_path)
    abs_target = os.path.abspath(target_path)
    abs_working_directory = os.path.abspath(working_directory)

    if not abs_target.startswith(abs_working_directory):
        return (
            f'Error: Cannot read "{file_path}" as it is outside the permitted directory'
        )

    if not os.path.isfile(abs_target):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(abs_target, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if len(file_content_string) < MAX_CHARS:
                return file_content_string
            if len(file_content_string) == MAX_CHARS:
                return file_content_string + (
                    f'...File "{file_path}" truncated at 10000 characters'
                )
    except Exception as e:
        return f"Error: {str(e)}"
