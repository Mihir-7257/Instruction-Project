
#  Interactive Equation Compiler

This is a simple compiler project written in Python. It takes arithmetic expressions or variable assignments from user input and compiles them into low-level

##  Project Structure

├── main.py             # Entry point for running the compiler
├── lexer.py            # Tokenizes input strings
├── parser.py           # Parses tokens into an Abstract Syntax Tree (AST)
├── codegenerator.py    # Converts the AST into custom instructions
├── test.py             # (Optional) Script for testing expressions
├── .gitignore          # Ignores unnecessary files

## How It Works

1. **Lexical Analysis**: `lexer.py` reads the input string and splits it into tokens (numbers, operators, variable names, etc.).
2. **Parsing**: `parser.py` turns those tokens into an AST (tree representation of the equation).
3. **Code Generation**: `codegenerator.py` walks the AST and outputs simple pseudo-assembly instructions.
4. **Execution**: `main.py` runs everything interactively and shows you both the instructions and evaluated result.


You'll see a prompt where you can enter expressions like:
x = 10
y = 20
x + y * 2


## Features

- Variable assignments (e.g., `a = 5`)
- Expressions using `+`, `-`, `*`, `/`
- Intermediate register-based instruction generation
- Stores variable values and reuses them
- Clear, commented output for learning purposes

## Example Output

**Input:**

```
x = 4
y = 2
x + y
```

**Output:**

```
Generated Instructions:
LOAD R0, 4                     ; Load constant 4
MOV R1, R0                     ; Store into variable x
LOAD R2, 2                     ; Load constant 2
MOV R3, R2                     ; Store into variable y
MOV R4, R1                     ; Load variable x
MOV R5, R3                     ; Load variable y
ADD R6, R4, R5                 ; Add R4 and R5

Evaluated Result: 6
##  .gitignore

This project includes a `.gitignore` that excludes:

- Python cache files (`__pycache__`)
- Virtual environments (`venv/`, `env/`)
- Editor config folders (`.vscode/`, `.idea/`)
- Output logs
