class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f'{self.employee_id}, {self.name}, {self.position}, {self.salary}'

class EmployeeManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def find_employee_by_id(self, employee_id):
        try:
            with open(self.file_path) as file:
                for line in file:
                    items = line.strip().split(', ')
                    if int(items[0]) == employee_id:
                        return Employee(int(items[0]), items[1], items[2], int(items[3]))
        except FileNotFoundError:
            print('File not found')
            return

    def add_employee(self):
        try:
            employee_id = int(input('Enter Employee ID: '))
        except ValueError:
            print('Please, enter a number')
            return
        if self.find_employee_by_id(employee_id):
            print('Employee ID already exists')
            return
        name = input('Enter Name: ')
        position = input('Enter Position: ')
        try:
            salary = int(input('Enter Salary: '))
        except ValueError:
            print('Please enter a number')
            return
        record = Employee(employee_id, name, position, salary)
        with open(self.file_path, 'a') as file:
            file.write(f'{record}\n')
        print('Employee record added')

    def view_all_employees(self):
        try:
            with open(self.file_path) as file:
                employees = file.readlines()
                if not employees:
                     print('There is no any employee records')
                else:
                    for employee in employees:
                        print(employee.strip())
        except FileNotFoundError:
            print('File not found')
            return

    def search_employee(self):
        try:
            employee_id = int(input('Enter Employee ID: '))
        except ValueError:
            print('Please, enter a number')
            return
        employee = self.find_employee_by_id(employee_id)
        if employee:
            print(employee)
        else:
            print('Employee not found')

    def update_employee(self):
        try:
            employee_id = int(input('Enter Employee ID: '))
        except ValueError:
            print('Please enter a number')
            return
        employee = self.find_employee_by_id(employee_id)
        if not employee:
            print('Employee not found')
            return
        name = input('New name: ')
        position = input('New position: ')
        try:
            salary = int(input('New salary: '))
        except ValueError:
            print('Please enter a number')
            return
        updated_record = f'{employee_id}, {name}, {position}, {salary}\n'
        try:
            with open(self.file_path, 'r') as file:
                lines = file.readlines()
            with open(self.file_path, 'w') as file:
                for line in lines:
                    if employee_id == int(line.strip().split(', ')[0]):
                        file.write(updated_record)
                    else:
                        file.write(line)
            print('Employee record updated')
        except FileNotFoundError:
            print('File not found')
            return

    def delete_employee(self):
        try:
            employee_id = int(input('Enter Employee ID: '))
        except ValueError:
            print('Please enter a number')
            return
        employee = self.find_employee_by_id(employee_id)
        if not employee:
            print('Employee not found')
        try:
            with open(self.file_path, 'r') as file:
                lines = file.readlines()
            with open(self.file_path, 'w') as file:
                for line in lines:
                    if int(line.strip().split(', ')[0]) != employee_id:
                        file.write(line)
            print('Employee record deleted')
        except FileNotFoundError:
            print('File not found')
            return

    def run(self):
        while True:
            print("""1. Add new employee record
2. View all employee records
3. Search for an employee by Employee ID
4. Update an employee's information
5. Delete an employee record
6. Exit""")

            try:
                choice = int(input('Enter your choice: '))
            except ValueError:
                print('Please, choose a number from 1 to 6')
                continue

            if choice == 1:
                self.add_employee()
            elif choice == 2:
                self.view_all_employees()
            elif choice == 3:
                self.search_employee()
            elif choice == 4:
                self.update_employee()
            elif choice == 5:
                self.delete_employee()
            elif choice == 6:
                print('Goodbye!')
                break
            else:
                print('Please, choose a number from 1 to 6')

if __name__ == '__main__':
    manager = EmployeeManager('employee.txt')
    manager.run()
