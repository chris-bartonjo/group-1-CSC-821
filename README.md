# CSC 821 — Group 1

Group project for **CSC 821: Design and Analysis of Algorithms**.
Each assigned module is developed on **its own branch** and lives in **its own folder**, then
merged into `main` at the end.

## Assigned modules

Each module is on its own branch (click to open it on GitHub):

| Module | Topic | Branch | Status |
|---|---|---|---|
| 4 | Radix Sort | [module-4-Radix-Sort](https://github.com/chris-bartonjo/group-1-CSC-821/tree/module-4-Radix-Sort) |  not started |
| 6 | Longest Common Subsequence (LCS) | [module-6-LCS](https://github.com/chris-bartonjo/group-1-CSC-821/tree/module-6-LCS) |  not started |
| 7 | Huffman Coding | [module-7-Huffman-coding](https://github.com/chris-bartonjo/group-1-CSC-821/tree/module-7-Huffman-coding) | ✅ done |
| 9 | FFT & Pattern Matching | [module-9-FFT-Pattern-Matching](https://github.com/chris-bartonjo/group-1-CSC-821/tree/module-9-FFT-Pattern-Matching) |  not started |
| 10 | NP-Completeness | [module-10-NP-Completeness](https://github.com/chris-bartonjo/group-1-CSC-821/tree/module-10-NP-Completeness) |  not started |

---

## Setup — do this once

### 1. Install VS Code
<https://code.visualstudio.com/>

### 2. Install Python 3
<https://www.python.org/downloads/> — on the first install screen, **tick “Add Python to PATH.”**
Then check it worked (open a terminal):
```bash
python --version
```

### 3. Install the VS Code extensions
In VS Code open **Extensions** (`Ctrl+Shift+X`) and install both (publisher: Microsoft):
- **Python**
- **Jupyter**

### 4. Clone the repo into a folder by opening a terminal window at the folder
```bash
git clone https://github.com/chris-bartonjo/group-1-CSC-821.git
cd group-1-CSC-821
```

### 5. Create and activate a virtual environment (venv) 
A **venv** is a private package folder for this project to keep your computer organized 
```bash
python -m venv .venv
```
Activate it:

| OS / shell | Command |
|---|---|
| Windows – PowerShell | `.venv\Scripts\Activate.ps1` |
| Windows – CMD | `.venv\Scripts\activate.bat` |
| macOS / Linux | `source .venv/bin/activate` |

When it’s active you’ll see `(.venv)` at the start of your prompt.
*(PowerShell blocking the script? Run once: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.)*

### 6. Install Jupyter
So VS Code can run the `.ipynb` notebooks in your venv:
```bash
pip install notebook ipykernel
```
*(A lab that needs extra libraries — e.g. `numpy`, `matplotlib` for the FFT module — lists them in its own folder.)*

---

## Run a lab notebook in VS Code
1. **File → Open Folder** and choose the cloned repo.
2. Switch to the module’s branch, e.g. `git checkout module-7-Huffman-coding`.
3. Open the module’s `.ipynb`.
4. Top-right **Select Kernel** → choose the **.venv** Python.
5. Click **Run All** (or step through with `Shift+Enter`).

Each module folder also includes a doc or pdf document for submission
