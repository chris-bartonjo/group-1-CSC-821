"""
nb_export.py - turn a Jupyter notebook (.ipynb) into a PDF or a Word file.

CSC 821 - Group 1.  No LaTeX needed.

HOW TO USE  (run these in a terminal, with your venv active):

    python nb_export.py my_notebook.ipynb            ->  makes my_notebook.pdf
    python nb_export.py my_notebook.ipynb --word     ->  makes my_notebook.docx

The file is created next to your notebook.
Tip: run the notebook in VS Code first (Run All) so its outputs are saved,
then export - otherwise the PDF/Word will not show the results.

WHAT YOU NEED:
    pip install nbconvert            (always)
    pip install pikepdf              (optional: makes the PDF preview on GitHub)
    Google Chrome or Microsoft Edge  (only for PDF)
    pandoc  ->  https://pandoc.org   (only for Word)
"""

import os
import sys
import subprocess
import tempfile
from pathlib import Path


def find_browser():
    """Return the path to Chrome or Edge, or stop with a clear message."""
    places = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",  # macOS
        "/usr/bin/google-chrome",                                        # Linux
    ]
    for place in places:
        if os.path.exists(place):
            return place
    sys.exit("Could not find Chrome or Edge. Please install one, then try again.")


def make_pdf(notebook, output):
    """notebook  ->  HTML (nbconvert)  ->  PDF (printed by a headless browser)."""
    browser = find_browser()
    # Work in a temporary folder so we don't leave an HTML file behind.
    with tempfile.TemporaryDirectory() as folder:
        html = Path(folder) / "page.html"

        # Step 1: notebook -> HTML
        subprocess.run(
            [sys.executable, "-m", "nbconvert", "--to", "html",
             "--output", "page", "--output-dir", folder, str(notebook)],
            check=True,
        )

        # Step 2: let the browser "print" that HTML to a PDF
        subprocess.run(
            [browser, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
             "--print-to-pdf=" + str(output), html.as_uri()],
            check=True,
        )

    # Optional tidy-up: rewrite the PDF so GitHub can preview it in the browser.
    try:
        import pikepdf
        temp = output.with_suffix(".tmp.pdf")
        with pikepdf.open(output) as pdf:
            pdf.save(temp, linearize=True)
        temp.replace(output)
    except Exception:
        pass  # pikepdf not installed - the PDF is still perfectly valid

    print("Made PDF:", output)


def make_word(notebook, output):
    """pandoc reads .ipynb directly and writes a Word (.docx) file."""
    try:
        subprocess.run(["pandoc", str(notebook), "-o", str(output)], check=True)
    except FileNotFoundError:
        sys.exit("Word export needs pandoc. Install it from https://pandoc.org")
    print("Made Word file:", output)


# ------------------------- main program -------------------------
if len(sys.argv) < 2:
    sys.exit("Usage: python nb_export.py notebook.ipynb [--word]")

# Use the full path so the PDF/Word is saved right next to the notebook.
notebook = Path(sys.argv[1]).resolve()
if not notebook.exists():
    sys.exit("File not found: " + str(notebook))

want_word = "--word" in sys.argv

if want_word:
    make_word(notebook, notebook.with_suffix(".docx"))
else:
    make_pdf(notebook, notebook.with_suffix(".pdf"))
