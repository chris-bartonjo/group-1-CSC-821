# CSC 821 — Module 6: Longest Common Subsequence (Group 1)

**CSC 821 — Group 1** · Status: done

Lab activity: a Python implementation of the **Longest Common Subsequence** using **dynamic
programming** — fill the DP table, read the length off the bottom-right cell, and trace the actual
subsequence back out — with the table printed step by step, a demonstration of why the table beats
plain recursion, two applications (DNA alignment and `git diff`), a space-optimised variant,
edge-case tests, and a timing check of the `O(m·n)` bound.

## Files
- `module_6_lcs.ipynb` — the notebook, runs top to bottom.
- `module_6_lcs.pdf` — rendered PDF of the executed notebook.
- `module_6_lcs.docx` — Word version of the same.

## The task

Write a Python function `lcs(s1, s2)` that returns the **length** of the longest subsequence common
to both strings **without rearranging** the order of characters, using dynamic programming.

1. Build a 2D table `dp` where `dp[i][j]` = length of the LCS of the first `i` characters of `s1`
   and the first `j` characters of `s2`.
2. Fill it with the recurrence:
   - If `s1[i-1] == s2[j-1]`: the LCS extends → `dp[i][j] = dp[i-1][j-1] + 1`
   - If `s1[i-1] != s2[j-1]`: drop one character from either string →
     `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`
3. The answer is in `dp[len(s1)][len(s2)]`.
4. Explain the dynamic-programming approach — optimal substructure, overlapping subproblems,
   and the `O(m·n)` time and space cost.

Sections 2–3 of the notebook cover steps 1–3; the explanation for step 4 runs through sections 2, 5
and 9 and is summarised in the conclusion.

## Run
```
jupyter notebook module_6_lcs.ipynb
```
or simply open the PDF.

## Re-export after editing

Run the notebook first (**Run All**) so the outputs are saved, then from the repo root:
```
python tools/nb_export.py module-6-lcs/module_6_lcs.ipynb           # PDF
python tools/nb_export.py module-6-lcs/module_6_lcs.ipynb --word    # Word
```

## Submission note

The LMS asks for the notebook named `Last_Firstname_LCS.ipynb`. The file is kept as
`module_6_lcs.ipynb` here to match the naming used by the other module folders — rename your copy
when uploading it.
