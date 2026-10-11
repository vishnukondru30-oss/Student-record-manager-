import json
import re
from pathlib import Path

DATA_FILE = Path("students.json")
EMAIL_PATTERN = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"


def valid_email(email):
    """Return True if email matches the basic email format."""
    return re.fullmatch(EMAIL_PATTERN, email) is not None


def load_students():
    """Read saved records from the JSON file."""
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            students = json.load(file)
        if not isinstance(students, list):
            raise ValueError("Student data file must contain a list.")
        return students
    except (json.JSONDecodeError, OSError, ValueError) as error:
        print(f"Could not read student records: {error}")
        return []


def save_students(students):
    """Save all student records to the JSON file."""
    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(students, file, indent=4)
        return True
    except OSError as error:
        print(f"Could not save student records: {error}")
        return False


def add_student():
    """Collect, validate, and save one student record."""
    try:
        name = input("Enter student name: ").strip()
        if not name:
            raise ValueError("Name cannot be empty.")

        roll_number = input("Enter roll number: ").strip()
        if not roll_number:
            raise ValueError("Roll number cannot be empty.")

        email = input("Enter email address: ").strip()
        if not valid_email(email):
            raise ValueError("Invalid email address. Example: student@example.com")

        age_text = input("Enter age: ").strip()
        age = int(age_text)
        if age <= 0:
            raise ValueError("Age must be a positive number.")

        students = load_students()
        if any(student.get("roll_number", "").lower() == roll_number.lower()
               for student in students):
            raise ValueError("This roll number already exists.")

        student = {
            "name": name,
            "roll_number": roll_number,
            "email": email,
            "age": age
        }
        students.append(student)

        if save_students(students):
            print("Student record added successfully!")

    except ValueError as error:
        print(f"Invalid input: {error}")
    except (EOFError, KeyboardInterrupt):
        print("\nInput cancelled.")


def display_students():
    """Read and display all saved student records."""
    students = load_students()

    if not students:
        print("No student records found.")
        return

    print("\n--- Saved Student Records ---")
    for number, student in enumerate(students, start=1):
        print(f"\nStudent {number}")
        print(f"Name       : {student.get('name', 'N/A')}")
        print(f"Roll Number: {student.get('roll_number', 'N/A')}")
        print(f"Email      : {student.get('email', 'N/A')}")
        print(f"Age        : {student.get('age', 'N/A')}")


def main():
    """Display the menu until the user chooses to exit."""
    while True:
        print("\n===== Student Record Manager =====")
        print("1. Add student")
        print("2. Display saved students")
        print("3. Exit")

        try:
            choice = input("Choose an option (1-3): ").strip()

            if choice == "1":
                add_student()
            elif choice == "2":
                display_students()
            elif choice == "3":
                print("Thank you for using Student Record Manager!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except (EOFError, KeyboardInterrupt):
            print("\nProgram closed.")
            break


if __name__ == "__main__":
    main()
