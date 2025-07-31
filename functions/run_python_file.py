

import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    absolute_working_directory = os.path.abspath(working_directory)
    full_file_path = os.path.abspath(os.path.join(absolute_working_directory, file_path))
    is_inside = os.path.commonpath([absolute_working_directory, full_file_path]) == absolute_working_directory

    if not is_inside:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(full_file_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    command = ['python', file_path] + args

    try:
        result = subprocess.run(command, 
                                stdout=subprocess.PIPE, 
                                stderr=subprocess.PIPE,
                                cwd=absolute_working_directory,
                                timeout=30,
                                text=True
                                )
        
        output = []

        if result.stdout.strip():
            output.append(f"STDOUT:\n{result.stdout.strip()}")
        
        if result.stderr.strip():
            output.append(f"STDERR:\n{result.stderr.strip()}")

        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")
        
        if not output:
            return "No output produced."

        return "\n\n".join(output)

    except subprocess.TimeoutExpired as e:
        return "Error: Process timed out after 30 seconds."
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute a Python file (`.py`) with optional arguments, constrained so the target file must reside within `working_directory`.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="Base directory; `file_path` must resolve inside this directory.",
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to `working_directory`. Must end with .py.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="List of command-line arguments to pass to the Python script.",
                items=types.Schema(type=types.Type.STRING),
                default=[],
            ),
        },
        required=["working_directory", "file_path"],
    ),
)