# Lab 3 Evidence

[Findings summary](findings_summary.md) records the coverage comparison and the Ruff warning and resolution. The results were transcribed from the student's terminal screenshots shared during the lab walkthrough.

## Screenshots to add

Save the original screenshots in this folder using these filenames:

| Filename | Required content |
|---|---|
| `coverage_before.png` | Initial `coverage report -m` output: `helpers.py` has 53 statements, 7 missed statements, 22 branch destinations, 7 partially covered branches, and 81% combined coverage. |
| `coverage_after.png` | Final coverage output: `helpers.py` has zero missed statements, zero partially covered branches, and 100% coverage. |
| `ruff_before.png` | Original E722 warning at `messy_module.py:44:5`. |
| `ruff_after.png` | Final Ruff output showing `All checks passed!`. |

The screenshots have not yet been added. Use your original saved images for the before results; rerunning the corrected code will show the after results.

## Proposal and remaining details

The [project proposal](../starting_the_project/project_proposal_template.md) is stored in the folder named by the lab README. Fill in the student name, student ID, and course fields, and confirm the proposed project scope before submission. Add your actual Week 1 comparison to the findings summary if required by your instructor.

## Optional HTML report

The generated HTML coverage report remains in `starter_code/htmlcov/` on your computer. Open its `index.html` locally. The coverage screenshots can serve as the repository evidence without uploading that generated folder.
