# ==============================================================================
# Task: Employee Salary Management System
# Author: Shagar
# File: shagar_employee_management.py
# Objective: Practice Python Functions and File Handling concepts.
# ==============================================================================

FILENAME = "employees.txt"


def add_employee(name, emp_id, salary, filename=FILENAME):
    """
    Function 1: Add Employee
    Takes employee name, ID, and salary as parameters.
    Opens the file in append mode ('a') and writes the record.
    Returns a success message.
    """
    record = f"{name} | {emp_id} | {salary}\n"
    with open(filename, "a", encoding="utf-8") as file:
        file.write(record)
    return "Employee Added Successfully"


def view_employees(filename=FILENAME):
    """
    Function 2: View Employees
    Opens the file in read mode ('r') and reads all employee records.
    Returns the list of employee records, or an empty list if file doesn't exist.
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            records = [line.strip() for line in file if line.strip()]
        return records
    except FileNotFoundError:
        return []


def display_menu():
    """
    Displays the main menu options to the user.
    Returns the user's selected choice.
    """
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Exit")
    print()
    choice = input("Choose Option: ").strip()
    return choice


def main():
    """
    Main application loop for Employee Salary Management System.
    """
    while True:
        print()
        choice = display_menu()
        print()

        if choice == "1":
            # Taking employee details from user
            name = input("Enter Name: ").strip()
            emp_id = input("Enter ID: ").strip()
            salary = input("Enter Salary: ").strip()

            # Calling reusable function to add employee
            message = add_employee(name, emp_id, salary)
            print()
            print(message)

        elif choice == "2":
            # Calling reusable function to retrieve records
            records = view_employees()
            print("--- Employee Records ---")
            if records:
                for record in records:
                    print(record)
            else:
                print("No employee records found in employees.txt.")
            print("------------------------")

        elif choice == "3":
            print("Exiting program. Thank you!")
            break

        else:
            print("Invalid option! Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
