# Lab 3: Code Coverage & Static Code Review — Student Kit

Everything in this folder is ready to run as-is. No setup beyond
installing the three tools below is needed.

## Folder contents

```
Lab3_Code_Coverage_StaticReview_StudentKit/
├── README.md                          <- this file, your lab walkthrough
├── requirements.txt                   <- pytest, coverage, ruff
├── starter_code/
│   ├── helpers.py                     <- target code (do not modify)
│   └── test_helpers_starter.py        <- your starting test suite
├── ruff_practice/
│   ├── messy_module.py                <- practice file for static analysis
│   └── pyproject.toml                 <- ruff rule configuration
└── starting_the_project/
    ├── pytodo_pro_student.zip         <- the full app for your semester project
    └── project_proposal_template.md   <- fill this in and submit
```

## 0. Setup (once per machine)

```powershell
pip install -r requirements.txt
pytest --version
coverage --version
ruff --version
```

---

## Step 1 — Run coverage.py and compare to your Week 1 table

```powershell
cd starter_code
coverage run --branch -m pytest -v
coverage report -m
```

Read the `Missing` column — those are the exact line numbers no test
touched. Open `helpers.py` and look at each one. Compare this to the
manual statement/branch estimate you traced by hand in Week 1: where
do the numbers disagree, and why?

Pay special attention to `parse_due_date` and `days_until_due` — they
currently have **no tests at all**, and `parse_due_date`'s `except`
block is exactly the kind of exception-handling path the lab slides
warn you about.

Optional — generate a browsable HTML report:

```powershell
coverage html
# then open htmlcov/index.html in a browser
```

## Step 2 — Raise branch coverage to ≥ 90%

In `test_helpers_starter.py`, add new test functions (do not delete
the existing ones) that close the gaps you found in Step 1. You will
need at least:

- A test for `add_days` with a **negative** `days` value.
- Tests for `is_valid_priority` with invalid/out-of-range/wrong-type
  input (`0`, `6`, a `float`, a `string`, `True`).
- Tests for `parse_due_date`: one valid date string, one malformed
  string that triggers the `except ValueError` branch, and the
  `fallback` behavior.
- A test for `days_until_due`.

Re-run until both numbers clear the bar:

```powershell
coverage run --branch -m pytest -v
coverage report -m
```

## Step 3 — Run ruff check and refactor

```powershell
cd ../ruff_practice
ruff check .
```

For each warning, note the rule code (e.g. `B006`), what it means,
and the line it points to — this is your findings summary deliverable.
Then try the automatic fixer:

```powershell
ruff check --fix .


ruff.exe check --fix --unsafe-fixes .
```

Review the diff, fix whatever remains by hand, and re-run `ruff check .`
until it reports no warnings.



## Deliverables checklist

- [ ] Coverage report (`coverage report -m` output, or the `htmlcov/`
      folder) showing statement and branch percentages before and
      after your changes.
- [ ] Updated `test_helpers_starter.py` reaching ≥ 90% branch coverage.
- [ ] A short before/after list of `ruff check` warnings and how each
      was resolved.
- [ ] One-page project proposal (`project_proposal_template.md`,
      filled in).
