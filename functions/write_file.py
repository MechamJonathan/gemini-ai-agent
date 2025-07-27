

import os


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