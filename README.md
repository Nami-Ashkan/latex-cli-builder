# LaTeX CLI Builder

A lightweight interactive Python command-line tool for compiling LaTeX projects with **pdfLaTeX**, **XeLaTeX**, or **LuaLaTeX**, with optional **BibTeX** and **Biber** support.

## Features

- Supports:
  - pdfLaTeX
  - XeLaTeX
  - LuaLaTeX
- Optional BibTeX and Biber workflows
- Automatically detects `.tex` files in the current directory
- Prompts the user when multiple `.tex` files are found
- Runs the required number of LaTeX compilation passes automatically
- Displays LaTeX logs only if compilation fails
- Optionally opens the generated PDF after a successful build
- Simple command-line interface

---

## Requirements

Before using this tool, make sure you have a LaTeX distribution installed and available in your system `PATH`.

Examples:

- **MiKTeX** (Windows)
- **TeX Live** (Windows, Linux, macOS)

The following executables should be available:

- `pdflatex`
- `xelatex`
- `lualatex`
- `bibtex`
- `biber` (if using Biber)

---

## Sample Files

The repository includes two example LaTeX documents.

### `sample.tex`

A minimal "Hello, World!" LaTeX document.

Use this file to quickly verify that the compiler is working correctly.

### `sample_2.tex`

A second example that uses the `amsmath` package and contains a few mathematical equations.

This demonstrates compilation of documents using additional packages.

---

## Using `main.exe`

1. Copy `main.exe` into the folder containing your `.tex` file(s).
2. Double-click `main.exe`.
3. If multiple `.tex` files are found, select the one you want to compile.
4. Choose the desired compilation method:
   - pdfLaTeX
   - XeLaTeX
   - LuaLaTeX
   - Optional BibTeX or Biber workflow
5. Wait for compilation to finish.
6. Press **Enter** to automatically open the generated PDF, or type anything and press **Enter** to skip opening it.

The generated PDF will be created in the same directory as the selected `.tex` file.

---

## Running from Python

If you prefer not to use the executable:

```bash
python main.py
```

or

```bash
py main.py
```

---

## Building `main.exe`

### 1. Install PyInstaller

```bash
pip install pyinstaller
```

### 2. Build the executable

```bash
pyinstaller --onefile --console main.py
```

After the build completes, the executable will be located in:

```
dist/main.exe
```

### Optional: Build with an icon

```bash
pyinstaller --onefile --console --icon=icon.ico main.py
```

---

## Project Structure

```
.
├── main.py
├── main.exe
├── sample.tex
├── sample_2.tex
├── README.md
└── dist/
```

---

## Notes

- Compilation logs are hidden during successful builds.
- If a compilation fails, the full LaTeX log is displayed to help with debugging.
- The tool does **not** include a LaTeX distribution. You must install MiKTeX or TeX Live separately.

---

## License

This project is released under the MIT License.
