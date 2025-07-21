
import os


def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)

    print(f"full path: {full_path}")
    print(os.path.abspath(directory))
    print(os.path.abspath(working_directory))

    if os.path.isdir(full_path):
        print("This is a directory!")
        print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    elif not os.path.exists(full_path):
        print(f'Error: "{directory}" is not a directory')
    else:
        print("this is working?")

    
