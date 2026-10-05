# Lab 3 — Coverage and Static Code Review Findings

## Coverage results

The following results refer to `helpers.py`, excluding the test file from the comparison.

| Measure | Before | After |
|---|---:|---:|
| Executable statements | 53 | 53 |
| Missed statements | 7 | 0 |
| Statement coverage | 86.8% | 100% |
| Branch destinations | 22 | 22 |
| Partially covered branches | 7 | 0 |
| Combined statement and branch coverage | 81% | 100% |

The initial report identified missing lines 36, 40, 47, 82, 109, 124, and 126. Additional tests covered invalid string inputs, a short truncation limit, missing email input, missing due dates, invalid due dates, and the default current-date behavior. The final report shows every statement and branch destination covered, exceeding the 90% branch coverage requirement. Existing tests were retained, and `helpers.py` was not modified.

## Static analysis findings

| Rule | Original location | Finding | Resolution |
|---|---|---|---|
| E722 | `ruff_practice/messy_module.py`, line 44 | A bare `except` catches all exceptions, including interruptions. | Replaced it with `except OSError` and explicitly returned `None` on file-access failure. |

The final Ruff check reported **All checks passed!**, with zero violations.

## Supporting evidence

- `coverage_before.png`: initial coverage report.
- `coverage_after.png`: final coverage report showing 100%.
- `ruff_before.png`: the original E722 warning.
- `ruff_after.png`: the final clean Ruff result.

## Week 1 comparison

[Add your actual Week 1 statement and branch estimates, compare them with the automated results, and explain any differences. Do not substitute combined coverage for a separate branch percentage.]
