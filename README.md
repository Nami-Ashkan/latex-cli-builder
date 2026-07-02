# LaTeX CLI Builder

A lightweight Python command-line tool for compiling LaTeX projects without manually typing compilation commands.

## Features

- Supports:
  - pdfLaTeX
  - XeLaTeX
  - LuaLaTeX
- Optional BibTeX or Biber workflows
- Automatically detects `.tex` files in the current directory
- Prompts when multiple `.tex` files are found
- Runs the required number of compilation passes automatically
- Displays LaTeX logs only if compilation fails
- Optionally opens the generated PDF after a successful build
- Works on Windows, macOS, and Linux
