# Module 4 — Radix Sort

**CSC 821 — Group 1** · Status: starter

## Lab: Implementing and Analyzing Radix Sort

**Objective.** Understand the Radix Sort algorithm by implementing it in Python. Sort a list of
phone numbers and analyze how the digits are sorted from the **least significant digit (LSD)** to
the **most significant digit (MSD)**, using **Counting Sort** as the per-digit subroutine.

**Scenario — sort these phone numbers ascending:**
```
[564, 213, 987, 432, 123, 765, 321, 654, 876]
```

### Tasks
1. Implement Radix Sort in Python.
2. Use Counting Sort as a helper function for each digit.
3. Sort the list and **display the array after each digit-level pass** (ones → tens → hundreds).
4. Analyze the intermediate and final results.

### Questions for reflection
1. What is the order of sorting for the digits in Radix Sort?
2. After sorting by the **least significant** digit, what does the intermediate array look like?
3. After sorting by the **most significant** digit, what is the final sorted output?

### Also covered — Medians & Order Statistics
- **Order statistics:** minimum (1st), maximum (last), **median** (middle), and the **k-th** element in sorted order.
- **Quickselect:** finds the k-th smallest like QuickSort but recurses into only one partition — **O(n) average**, O(n²) worst.
- **Median of Medians:** picks a good pivot (median of groups of 5) to guarantee **O(n) worst-case** selection.
- **Applications:** percentiles, top-k selection, median filtering, database median/percentile queries, k-NN.

### Deliverable
The notebook (`module_4_radix_sort.ipynb`) and its exported **PDF** (make it with `tools/nb_export.py`).
Work on the branch `module-4-Radix-Sort`, then merge into `main`. **Submit PDF only.**
