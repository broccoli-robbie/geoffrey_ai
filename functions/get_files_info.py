import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        abs_working_directory: str = os.path.abspath(working_directory)
        abs_target = os.path.abspath(os.path.join(abs_working_directory, directory))

        if not abs_target.startswith(abs_working_directory):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(abs_target):
            return f'Error: "{directory}" is not a directory'

        files: list[str] = os.listdir(abs_target)
        files_info: list[str] = []
        for file in files:
            filepath: str = os.path.join(abs_target, file)
            is_dir = os.path.isdir(filepath)
            file_size = os.path.getsize(filepath)
            files_info.append(f"- {file}: file_size={file_size} bytes, is_dir={is_dir}")
        return "\n".join(files_info)
    except Exception as e:
        return f"Error: listing files: {e}"


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
