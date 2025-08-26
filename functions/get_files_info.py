import os
from google.genai import types


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)


def get_files_info(working_directory, directory="."):
    abs_working_directory = os.path.abspath(working_directory)
    abs_target = os.path.abspath(os.path.join(working_directory, directory))

    if not abs_target.startswith(abs_working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working_directory'

    if not os.path.isdir(abs_target):
        return f'Error: "{directory}" is not a directory'

    try:
        targets = os.listdir(abs_target)
        lines = []
        for target in targets:
            target_path = os.path.join(abs_target, target)
            lines.append(
                f"- {target}: file_size={os.path.getsize(target_path)}, is_dir={os.path.isdir(target_path)}"
            )
        return "\n".join(lines)
    except Exception as e:
        return f"Error: {str(e)}"
