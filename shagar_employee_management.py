# Task: Employee Salary Management System
# Name: Shagar
# File: shagar_employee_management.py

# Function 1: Add Employee
def add_employee(name, emp_id, salary):
    # Open file in append mode ('a') to add new data
    with open("employees.txt", "a") as file:
        file.write(f"{name} | {emp_id} | {salary}\n")
    return "Employee Added Successfully"


# Function 2: View Employees
def view_employees():
    # Open file in read mode ('r') to read data
    try:
        with open("employees.txt", "r") as file:
            data = file.read()
        return data
    except FileNotFoundError:
        return "No employee records found.\n"


# Main Program
while True:
    # Display Menu
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Exit")
    print()

    choice = input("Choose Option: ")

    # Option 1: Add Employee
    if choice == "1":
        print()
        name = input("Enter Name: ")
        emp_id = input("Enter ID: ")
        salary = input("Enter Salary: ")
        print()

        # Call function and display return message
        message = add_employee(name, emp_id, salary)
        print(message)
        print()

    # Option 2: View Employees
    elif choice == "2":
        print()
        records = view_employees()
        print(records)

    # Option 3: Exit
    elif choice == "3":
        print()
        print("Exiting program.")
        break

    # Invalid Option
    else:
        print()
        print("Invalid option! Please enter 1, 2, or 3.")
        print()
