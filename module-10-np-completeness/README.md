# Module 10 — NP-Completeness

**CSC 821 — Group 1** · Status:  not started

## Lab: Exploring NP-Complete Problems and Reductions

**Objective.** Demonstrate an understanding of **NP-completeness** through problem analysis,
a **polynomial-time reduction**, and an algorithm implementation.

### Steps
1. **Problem selection.** Choose one NP-complete problem: **3-SAT**, **Vertex Cover**, or **Subset Sum**.
2. **Understanding.** Give its formal definition, explain **why it is NP-complete**, and note real-world applications.
3. **Reduction.** Demonstrate a **polynomial-time reduction** (from a known NP-complete problem), documenting each step and the logic.
4. **Implementation.** Implement a solver for your chosen problem:
   - **3-SAT** → backtracking
   - **Vertex Cover** → greedy
   - **Subset Sum** → recursion
5. Include a clear problem explanation, the reduction write-up, **commented code**, and **sample input/output**.

### Background to reference
- **NP** = solutions verifiable in polynomial time; **NP-complete** = in NP *and* every NP problem reduces to it.
- **Cook–Levin theorem:** SAT was the first proven NP-complete problem.
- **Reductions** prove hardness: if a known NP-complete problem reduces to yours, yours is at least as hard.
- When exact solving is infeasible: **approximation algorithms**, **heuristics/metaheuristics**, or restricting the input.

### Deliverable
A Python or Jupyter file with the explanation, reduction, commented code, and sample I/O — exported to **PDF** (`tools/nb_export.py`). **Upload PDF only.**
Work on the branch `module-10-NP-Completeness`, then merge into `main`.
