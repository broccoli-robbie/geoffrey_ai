import os
from google.genai import types


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes files to the specified directory, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The name of a file in the working directory that will be written to or overwritten with the specified content.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write or overwrite to the specified file.",
            ),
        },
    ),
)


def write_file(working_directory, file_path, content):
    target_path = os.path.join(working_directory, file_path)
    abs_target = os.path.abspath(target_path)
    abs_working_directory = os.path.abspath(working_directory)
    target_dir = os.path.dirname(abs_target)

    if not abs_target.startswith(abs_working_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        with open(abs_target, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {str(e)}"
