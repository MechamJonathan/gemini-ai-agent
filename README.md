# AI Agent (Toy Claude Code)

A simple AI-powered coding agent built with Python and Google’s free Gemini API. Inspired by tools like Cursor and Claude Code. 

## What does the Agent Do?
This program is a CLI tool that accepts a coding task and works toward completing it by calling a set of predefined functions.

Example workflow:
1. Accepts a coding task:
  ```
  uv run main.py "fix my calculator app, its not starting correctly"
  ```
2. Chooses from a set of built-in tools:
  - Scan files in a directory
  - Read a file’s contents
  - Overwrite a file’s contents
  - Run a Python file
3. Iteratively repeats step 2 until the task is completed

Example Output:
```
# Calling function: get_files_info
# Calling function: get_file_content
# Calling function: write_file
# Calling function: run_python_file
# Calling function: write_file
# Calling function: run_python_file
# Final response:
# Great! The calculator app now seems to be working correctly. The output shows the expression and the result in a formatted way.
```

## Prerequisites
Before running this project, make sure you have:
- Python 3.10+ installed
- uv project & package manager installed
- Access to a Unix-like shell (zsh, bash, etc.)

## Installation & Usage
1. Clone the repository:
```
git clone https://github.com/your-username/ai-agent.git
cd ai-agent
```
2. Install dependencies with uv:
```
uv sync
```
3. Run the agent with a coding task:
```
uv run main.py "fix my calculator app"
```
## Limitations
- This is a toy agent, so expect it to fail sometimes.
- Requires a Gemini API key (free tier works).
- The agent only supports Python projects for execution.

