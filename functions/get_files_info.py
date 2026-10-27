import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        abs_working_directory: str = os.path.abspath(working_directory)
        abs_target = os.path.abspath(os.path.join(abs_working_directory, directory))

        if not abs_target.startswith(abs_working_directory):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(abs_target):
            return f'Error: "{directory}" is not a directory'

        targets: list[str] = os.listdir(abs_target)
        lines: list[str] = []
        for target in targets:
            target_path: str = os.path.join(abs_target, target)
            lines.append(
                f"- {target}: file_size={os.path.getsize(target_path)}, is_dir={os.path.isdir(target_path)}"
            )
        return "\n".join(lines)
    except Exception as e:
        return f"Error: {e}"


schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}
