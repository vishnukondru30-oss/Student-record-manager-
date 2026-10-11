# Student Record Manager

A beginner-friendly Python console application for storing and viewing student records.

## Features
- Add student name, roll number, email, and age
- Validate email addresses using Python Regex (`re`)
- Save records to `students.json`
- Read and display saved records
- Handle invalid inputs and file/JSON errors using exceptions
- Prevent duplicate roll numbers

## Requirements
- Python 3.8 or later
- No third-party packages required

## How to run
1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python main.py
   ```

   On some Windows systems, use `py main.py`.

## How it works
- `valid_email()` checks the email format with a regular expression.
- `add_student()` validates user input and adds a record.
- `save_students()` writes records to `students.json`.
- `load_students()` reads existing records.
- `display_students()` prints saved records.
- `try`/`except` blocks handle invalid input and file errors.

## Example email formats
- Valid: `student@example.com`
- Invalid: `studentexample.com`

## GitHub submission
1. Sign in to [GitHub](https://github.com/).
2. Click **New repository**.
3. Name it `student-record-manager`.
4. Choose **Public** if your instructor needs to access it.
5. Create the repository.
6. Upload `main.py` and `README.md` (and optionally `.gitignore`) using **Add file → Upload files**.
7. Click **Commit changes**.
8. Copy your repository URL and submit it.

Your link will look like: `https://github.com/YOUR-USERNAME/student-record-manager`

Note: `students.json` is created automatically the first time a record is saved. It does not need to be uploaded with the project.
