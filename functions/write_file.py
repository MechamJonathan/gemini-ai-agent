import os
from google.genai import types

def write_file(working_directory, file_path, content):
    absolute_working_directory = os.path.abspath(working_directory)
    full_file_path = os.path.abspath(os.path.join(absolute_working_directory, file_path))
    is_inside = os.path.commonpath([absolute_working_directory, full_file_path]) == absolute_working_directory

    if not is_inside:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    os.makedirs(os.path.dirname(full_file_path), exist_ok=True)

    try:
        with open(full_file_path, 'w') as file:
            file.write(content)
        return f'Successfully wrote to \"{file_path}\" ({len(content)} characters written)'
    except IOError as e:
        return f"Error: writing to file: {e}"
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write `content` to `file_path`, constrained to be inside `working_directory`.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="The base directory; the target file must reside within this directory (resolved absolutely).",
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path of the file to write, relative to `working_directory`.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The string content to write into the file.",
            ),
        },
        required=["working_directory", "file_path", "content"],
    ),
)