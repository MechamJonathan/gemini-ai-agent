import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    absolute_working_directory = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(absolute_working_directory, directory))
    is_inside = os.path.commonpath([absolute_working_directory, full_path]) == absolute_working_directory
    result = []

    if not is_inside:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'
    
    contents = os.listdir(full_path)

    for item in contents:
        try:
            full_item_path = os.path.join(full_path, item)
            file_size = os.path.getsize(full_item_path)
            is_dir = os.path.isdir(full_item_path)
            result.append(f"- {item}: file_size={file_size} bytes, is_dir={is_dir}")
        except OSError as e:
            result.append(f"- {item}: error reading file info ({e})")
    return "\n".join(result)

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

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
    ]
)
    
