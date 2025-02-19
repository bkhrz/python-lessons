def find_employee_by_id(employee_id):
    with open('employees.txt', 'r') as f:
        for line in f:
            items = line.strip().split(', ')
            if int(items[0]) == employee_id:
                return items

def add_employee():
    employee_id = int(input('ID: '))
    if find_employee_by_id(employee_id):
        print("Employee ID already exists. Please use a unique ID.")
        return
    name = input('Name: ')
    position = input('Position: ')
    salary = int(input('Salary: $'))
    with open('employees.txt', 'a') as f:
        f.write(f'{employee_id}, {name}, {position}, {salary}\n')
    print("Employee record added successfully.")

def view_all_employees():
    with open('employees.txt', 'r') as f:
        employees = f.readlines()
        if not employees:
            print("No employee records found.")
        else:
            for employee in employees:
                print(employee.strip())

def search_employee():
    employee_id = int(input('Enter the ID to find employee: '))
    employee = find_employee_by_id(employee_id)
    if employee:
        print(employee)
    else:
        print("Employee not found")

def update_employee():
    employee_id = int(input('Enter the ID to update employee: '))
    employee = find_employee_by_id(employee_id)
    if not employee:
        print("Employee not found")
        return
    name = input(f'New name: ')
    position = input(f'New position: ')
    salary = input(f'New salary : ')
    updated_record = f'{employee_id}, {name}, {position}, {salary}\n'

    with open('employees.txt', 'r') as f:
        lines = f.readlines()
    with open('employees.txt', 'w') as f:
        for line in lines:
            if int(line.split(', ')[0]) == employee_id:
                f.write(updated_record)
            else:
                f.write(line)
    print("Employee record updated")

def delete_employee():
    employee_id = int(input('Enter the ID to delete employee: '))
    with open('employees.txt', 'r') as f:
        lines = f.readlines()
    with open('employees.txt', 'w') as f:
        for line in lines:
            if int(line.split(', ')[0]) != employee_id:
                f.write(line)
            else:
                pass


while True:
    print("""1. Add new employee record
2. View all employee records
3. Search for an employee by Employee ID
4. Update an employee's information
5. Delete an employee record
6. Exit""")

    try:
        choice = int(input('Choose your option from 1 to 6: '))
    except ValueError:
        print('Please enter a number from 1 to 6.')
        continue

    if choice == 1:
        add_employee()
    elif choice == 2:
        view_all_employees()
    elif choice == 3:
        search_employee()
    elif choice == 4:
        update_employee()
    elif choice == 5:
        delete_employee()
    elif choice == 6:
        print("Exited")
        break
    else:
        print("Please enter a number from 1 to 6.")