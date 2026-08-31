# Module 9 — FFT & Pattern Matching

**CSC 821 — Group 1** · Status: ⏳ not started

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
- Two Python scripts: `fft_last_firstname.py` and `pattern_matching_last_firstname.py`.
- A brief **1–2 page report** summarizing findings and experiences.

### Evaluation
- **Implementation** — correctness and efficiency.
- **Documentation** — clear comments and code structure.
- **Analysis** — depth of understanding in the summaries.

### Notes
Needs `numpy` and `matplotlib` (already in `requirements.txt`).
Work on the branch `module-9-FFT-Pattern-Matching`, then merge into `main`. Submit the scripts and report on the LMS.
