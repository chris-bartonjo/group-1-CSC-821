# Module 6 — Longest Common Subsequence (LCS)

**CSC 821 — Group 1** · Status: done

## Lab: Longest Common Subsequence (LCS)

**Problem.** Implement a **dynamic programming** solution to find the Longest Common Subsequence
between two strings `s1` and `s2` — the longest subsequence common to both **without rearranging**
the order of characters.

**Task.** Write a Python function `lcs(s1, s2)` that returns the **length** of the LCS using DP.

### Steps
1. Build a 2D table `dp` where `dp[i][j]` = length of the LCS of the first `i` characters of `s1`
   and the first `j` characters of `s2`.
2. Fill it with the recurrence:
   - If `s1[i-1] == s2[j-1]`: the LCS extends → `dp[i][j] = dp[i-1][j-1] + 1`
   - If `s1[i-1] != s2[j-1]`: drop one character from either string →
     `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`
3. The answer (LCS length) is in `dp[len(s1)][len(s2)]`.
4. Give a **brief explanation** of the dynamic-programming approach (optimal substructure +
   overlapping subproblems; each cell built from already-computed neighbours; time & space `O(m·n)`).

### Instructions
- Use a **Colab or Jupyter** notebook.
- Name the notebook `Last_Firstname_LCS.ipynb`.
- Submit the notebook on the LMS.

### Deliverable
The notebook (`Last_Firstname_LCS.ipynb`) and, if useful, its exported PDF/Word (`tools/nb_export.py`).
Work on the branch `module-6-LCS`, then merge into `main`.
