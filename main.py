import subprocess
import sys
import os
import glob
import subprocess

os.system("cls")

def run(cmd):
    """Run LaTeX command silently, show output only on failure."""
    #print(f"> {' '.join(cmd)}")

    result = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )

    if result.returncode != 0:
        print("\n[-] Command failed:\n")
        print(result.stdout)   # show full LaTeX log only on failure
        return False

    return True

def select_tex_file():
    tex_files = glob.glob("*.tex")

    if not tex_files:
        print("[-] No .tex files found in current directory.")
        return None, None

    # If only one file, auto-select it
    if len(tex_files) == 1:
        texfile = tex_files[0]
        jobname = os.path.splitext(texfile)[0]
        print(f"[+] Only one .tex file found: {texfile}")
        return texfile, jobname

    # Multiple files → prompt user
    print("\n[+] Multiple .tex files found:\n")
    for i, f in enumerate(tex_files, start=1):
        print(f"[{i}] {f}")

    print("[0] Exit\n")

    while True:
        choice = input("Select file: ").strip()

        if choice == "0":
            print("[!] Exiting.")
            return None, None

        if choice.isdigit() and 1 <= int(choice) <= len(tex_files):
            texfile = tex_files[int(choice) - 1]
            jobname = os.path.splitext(texfile)[0]
            return texfile, jobname

        print("[-] Invalid choice. Try again.")

def prompt_open_pdf(pdf_file):
    print("\n[+] Compilation finished successfully.")
    choice = input("Press Enter to open the PDF, or type anything + Enter to skip: ")

    if choice.strip() != "":
        print("[!] Skipping PDF opening.")
        return

    if not os.path.exists(pdf_file):
        print("[-] PDF file not found.")
        return

    print(f"[+] Opening {pdf_file}...")

    try:
        if sys.platform.startswith("win"):
            os.startfile(pdf_file)
        elif sys.platform.startswith("darwin"):
            subprocess.run(["open", pdf_file])
        else:
            subprocess.run(["xdg-open", pdf_file])
    except Exception as e:
        print(f"[-] Failed to open PDF: {e}")




def choose():
    print("============================================")
    print("          LaTeX PDF Compiler")
    print("============================================\n")
    print("Choose compilation method:\n")
    print("[1] pdfLaTeX")
    print("[2] XeLaTeX")
    print("[3] LuaLaTeX\n")
    print("[4] pdfLaTeX + BibTeX")
    print("[5] XeLaTeX + BibTeX")
    print("[6] LuaLaTeX + BibTeX\n")
    print("[7] pdfLaTeX + Biber")
    print("[8] XeLaTeX + Biber")
    print("[9] LuaLaTeX + Biber\n")
    print("[0] Exit\n")

    choice = input("Enter your choice: ").strip()

    mapping = {
        "1": ("pdflatex", None),
        "2": ("xelatex", None),
        "3": ("lualatex", None),
        "4": ("pdflatex", "bibtex"),
        "5": ("xelatex", "bibtex"),
        "6": ("lualatex", "bibtex"),
        "7": ("pdflatex", "biber"),
        "8": ("xelatex", "biber"),
        "9": ("lualatex", "biber"),
        "0": (None, None),
    }

    return mapping.get(choice, (None, None))

def get_run_count(bibtool):
    if bibtool is None:
        return 2
    return 3

def compile_latex(engine, bibtool, texfile, jobname):
    runs = get_run_count(bibtool)

    print(f"[+] Running {runs} LaTeX compilation(s)\n")

    # First compile
    if not run([engine, "-interaction=nonstopmode", texfile]):
        print("[-] First compilation failed.")
        return False

    # Bibliography step (if needed)
    if bibtool == "bibtex":
        print("\n[+] Running BibTeX...")
        if not run(["bibtex", jobname]):
            print("[-] BibTeX failed.")
            return False

    elif bibtool == "biber":
        print("\n[+] Running Biber...")
        if not run(["biber", jobname]):
            print("[-] Biber failed.")
            return False

    # Remaining LaTeX runs
    for i in range(2, runs + 1):
        print(f"\n[+] LaTeX compilation {i}...")
        if not run([engine, "-interaction=nonstopmode", texfile]):
            print(f"[-] Compilation {i} failed.")
            return False

    print(f"\n[+] PDF generated successfully: {jobname}.pdf\n")
    return True


def main():

    TEXFILE, JOBNAME = select_tex_file()

    if TEXFILE is None:
        sys.exit(1)

    compiler, bibtool = choose()

    if compiler is None and bibtool is None:
        print("[!] Exiting.")
        sys.exit(0)

    if compiler is None:
        print("[-] Invalid choice.")
        sys.exit(1)

    print(f"\n[+] Selected compiler: {compiler}")
    print(f"[+] Bibliography tool: {bibtool or 'none'}\n")

    success = compile_latex(compiler, bibtool, TEXFILE, JOBNAME)

    if not success:
        sys.exit(1)
    
    os.system("cls")
    prompt_open_pdf(f"{JOBNAME}.pdf")


if __name__ == "__main__":
    main()
