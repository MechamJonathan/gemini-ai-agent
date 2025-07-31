import os
from google.genai import types

def get_file_content(working_directory, file_path):
    absolute_working_directory = os.path.abspath(working_directory)
    full_file_path = os.path.abspath(os.path.join(absolute_working_directory, file_path))
    is_inside = os.path.commonpath([absolute_working_directory, full_file_path]) == absolute_working_directory

    if not is_inside:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(full_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        MAX_CHARS = 10000
        with open(full_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS + 1)

        if len(file_content_string) > MAX_CHARS:
            truncation_notice = f'\n[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return file_content_string[:MAX_CHARS] + truncation_notice
        else:
            return file_content_string[:MAX_CHARS]
    except OSError as e:
        return f'Error: Cannot read "{file_path}" contents. {str(e)}'


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read up to the first 10,000 characters of a file, constrained so the target file must reside within `working_directory`.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="Base directory; `file_path` must resolve inside this directory.",
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to read, relative to `working_directory`.",
            ),
        },
        required=["working_directory", "file_path"],
    ),
)