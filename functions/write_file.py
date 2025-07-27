

import os


def write_file(working_directory, file_path, content):
    absolute_working_directory = os.path.abspath(working_directory)
    full_file_path = os.path.abspath(os.path.join(absolute_working_directory, file_path))
    is_inside = os.path.commonpath([absolute_working_directory, full_file_path]) == absolute_working_directory


    if not is_inside:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(full_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
