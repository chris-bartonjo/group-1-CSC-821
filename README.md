# CSC 821 — Group 1

Group project for **CSC 821: Design and Analysis of Algorithms**.
Each assigned module is developed on **its own branch** and lives in **its own folder**, then
merged into `main` at the end.

## Assigned modules

Each module is on its own branch (click to open it on GitHub):

| Module | Topic | Branch | Status |
|---|---|---|---|
| 4 | Radix Sort | [module-4-Radix-Sort](https://github.com/chris-bartonjo/group-1-CSC-821/tree/module-4-Radix-Sort) | ⏳ not started |
| 6 | Longest Common Subsequence (LCS) | [module-6-LCS](https://github.com/chris-bartonjo/group-1-CSC-821/tree/module-6-LCS) | ⏳ not started |
| 7 | Huffman Coding | [module-7-Huffman-coding](https://github.com/chris-bartonjo/group-1-CSC-821/tree/module-7-Huffman-coding) | ✅ done |
| 9 | FFT & Pattern Matching | [module-9-FFT-Pattern-Matching](https://github.com/chris-bartonjo/group-1-CSC-821/tree/module-9-FFT-Pattern-Matching) | ⏳ not started |
| 10 | NP-Completeness | [module-10-NP-Completeness](https://github.com/chris-bartonjo/group-1-CSC-821/tree/module-10-NP-Completeness) | ⏳ not started |

*A branch link only works once that branch has been pushed — so far only **Module 7** exists.*
Finished lab: **[module-7-huffman-coding/](https://github.com/chris-bartonjo/group-1-CSC-821/tree/module-7-Huffman-coding/module-7-huffman-coding)** (notebook + PDF).

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

### 4. Clone the repo
```bash
git clone https://github.com/chris-bartonjo/group-1-CSC-821.git
cd group-1-CSC-821
```

### 5. Create and activate a virtual environment (venv)
A **venv** is a private package folder for this project, so its libraries don’t clash with the
rest of your system.
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

### 7. (Optional) environment variables — `.env`
These algorithm labs need no secrets, but if one ever needs configuration, copy the template:
```bash
cp .env.example .env      # Windows: copy .env.example .env
```
`.env` is git-ignored, so your local values are never committed.

---

## Run a lab notebook in VS Code
1. **File → Open Folder** and choose the cloned repo.
2. Switch to the module’s branch, e.g. `git checkout module-7-Huffman-coding`.
3. Open the module’s `.ipynb`.
4. Top-right **Select Kernel** → choose the **.venv** Python.
5. Click **Run All** (or step through with `Shift+Enter`).

Each module folder also includes a **PDF** if you just want to read the finished notebook.

---

## Working on your module (group members)
```bash
git checkout main
git pull
git checkout -b module-4-Radix-Sort        # your module's branch
#   ... do the work inside module-4-radix-sort/ ...
git add .
git commit -m "Module 4: Radix Sort lab"
git push -u origin module-4-Radix-Sort
```
Open a pull request into `main` when your lab is ready — we merge everyone’s branch at the end.
