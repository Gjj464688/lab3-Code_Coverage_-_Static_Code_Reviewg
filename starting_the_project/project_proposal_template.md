# Project Proposal — PyTodo Pro

**Student name:** [Enter your name]  
**Student ID:** [Enter your student ID]  
**Course / section:** [Enter your course and section]  
**Repository:** https://github.com/Gjj464688/lab3-Code_Coverage_-_Static_Code_Reviewg

## Problem and intended users
Students need a simple way to track assignments and personal tasks, identify urgent work, and avoid missed deadlines. This project proposes a Python task manager for individual students, with a focus on reliable date handling, input validation, and maintainable code.

## Objectives and scope
The application will let a user add, view, edit, delete, and complete tasks. Each task will have a title, a priority from 1 to 5, an optional due date, and a completion status. Users will be able to filter tasks by status, sort them by priority or due date, and view overdue tasks. Missing or invalid input will produce a clear message instead of an unexpected failure.

The proposed first version will use a simple command-line interface and a local JSON file to retain tasks between sessions. Accounts, cloud synchronization, and notifications are outside the initial scope.

## Implementation approach
Python will provide the task-management logic, using `datetime` for date calculations and `json` for local storage. The existing helper functions will be reused where appropriate. Task logic, storage, and the interface will be kept in separate modules so they can be tested independently.

## Testing and quality assurance
Pytest will verify normal operations, boundary values, wrong input types, invalid dates, and file-access failures. Coverage.py will measure statement and branch coverage separately, with a target of at least 90% for the core application logic. Ruff will check the Python source, and all reported violations will be reviewed and resolved. Tests will run again after changes to detect regressions.

## Milestones and deliverables
1. Confirm requirements and define the task data model.
2. Implement task operations and local storage.
3. Complete the interface, validation, and automated tests.
4. Review coverage and Ruff results, then prepare documentation and a demonstration.

Final deliverables will include source code, automated tests, coverage and Ruff evidence, setup instructions, and a short demonstration. Success means tasks persist correctly, planned operations work, invalid input is handled predictably, and the quality targets are met.
