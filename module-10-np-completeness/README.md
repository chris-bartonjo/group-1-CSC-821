# CSC 821 — Module 10: NP-Completeness (Group 1)

**Lab:** Exploring NP-Complete Problems and Reductions.
**Chosen problem:** **Vertex Cover** — its formal definition, why it is NP-complete (membership in
NP plus a polynomial-time reduction from 3-SAT), real-world applications, the documented and
verified **3-SAT ≤ₚ Vertex Cover** reduction with a graph diagram, and a greedy 2-approximation
solver with sample input/output.

## Group members and roles

| # | Name | Reg. No. |
|---|---|---|
| 1 | Nyabuto Pharminous | ST62/56180/2025 |
| 2 | Obed Munyao | ST62/61043/2025 |
| 3 | Thomas Kibet Yebei | ST62/59650/2025 |
| 4 | Ferdinand Atila Luvembe | ST62/60337/2025 |
| 5 | Samson Wangila Wanyonyi | ST62/60771/2025 |
| 6 | Thomas Kimani Miringu | ST62/61244/2025 |
| 7 | Samuel Abuko Abuti | ST62/59655/2025 |
| 8 | Githinji Lucy Njeri | ST62/60682/2025 |
| 9 | Haron Samoei | ST62/60356/2025 |
| 10 | Simon Mwangi Maina | ST62/61647/2025 |
| 11 | Brian Cheruiyot | ST62/61027/2025 |
| 12 | Susan Wambui | ST62/60422/2025 |
| 13 | Awello Kanyandong Kevins | ST62/61033/2025 |
| 14 | Patrick Mwangi Wanjiru | ST62/59698/2025 |
| 15 | Stephen Mwangi Mumbi | ST62/59653/2025 |
| 16 | Abisagy Nafula Wanyonyi | ST62/56881/2025 |

**Roles.** The group worked collaboratively: members shared the problem research and the write-up of
the definition, the NP-completeness argument, and the 3-SAT reduction, while others focused on the
Python implementation (the greedy solver and the reduction/verification code), the sample runs, and
assembling the documentation and this submission.

## Files
- `module_10_np_completeness.ipynb` — problem explanation, the 3-SAT → Vertex Cover reduction, the greedy solver, and sample input/output (runs top to bottom).
- `module_10_np_completeness.pdf` / `.docx` — rendered versions of the notebook.

No external CSV datasets are needed — the notebook builds its own problem instances.

## Run
```
jupyter notebook module_10_np_completeness.ipynb
```
or open the PDF/Word version.
