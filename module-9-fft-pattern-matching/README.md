# Module 9 — FFT & Pattern Matching

**CSC 821 — Group 1** · Status: done

## Lab: Fast Fourier Transform (FFT) and Pattern Matching Algorithms

**Objective.** Implement the **Fast Fourier Transform** and three **pattern-matching** algorithms
(Naive, KMP, Boyer-Moore) in Python, and understand their applications and efficiencies.

### Part 1 — Fast Fourier Transform (FFT)
- Implement the FFT algorithm **from scratch** (a Python function).
- Create a test signal (e.g. a **sine wave**) and use FFT to analyze its **frequency components**.
- **Plot** the original signal and its frequency spectrum with **Matplotlib**.
- **Output:** `fft_last_firstname.py` + a plot (signal and its FFT).
- **Summary:** explain the FFT algorithm and why it matters in signal processing.

### Part 2 — Pattern Matching (Naive, KMP, Boyer-Moore)
- Write **three separate functions**, one per algorithm.
- Test each with a sample **text** and **pattern**; display the **indices** where matches are found.
- Discuss the **time complexity** of each and when each is preferred.
- **Output:** `pattern_matching_last_firstname.py` with all three algorithms and test cases.
- **Summary:** compare the three algorithms' efficiencies and their use cases in text processing.

### Deliverables
- One Jupyter notebook containing both implementations, demonstrations,
  validation, and plots: `group-1-CSC-821.ipynb`.
- A separate written report: `REPORT.pdf`.
- The generated signal and frequency-spectrum plot: `fft_signal_spectrum.png`.

### Evaluation
- **Implementation** — correctness and efficiency.
- **Documentation** — clear comments and code structure.
- **Analysis** — depth of understanding in the summaries.

### Notes
Needs `numpy` and `matplotlib` (already in `requirements.txt`).
Work on the branch `module-9-FFT-Pattern-Matching`, then merge into `main`. Submit the scripts and report on the LMS.

### Completed files

- `group-1-CSC-821.ipynb` — recursive radix-2 FFT, signal analysis, Naive Search,
  KMP, Boyer-Moore, validation checks, and plots.
- `REPORT.pdf` — two-page discussion of the algorithms, complexity, results,
  applications, and findings.
- `fft_signal_spectrum.png` — generated signal and frequency-spectrum figure.

### Run

Open `group-1-CSC-821.ipynb` in VS Code, select the module's `.venv` kernel, and choose
**Run All**. From the repository root, the notebook can also be executed with:

```powershell
& 'module-9-fft-pattern-matching\.venv\Scripts\jupyter.exe' execute 'module-9-fft-pattern-matching\group-1-CSC-821.ipynb' --inplace
```
