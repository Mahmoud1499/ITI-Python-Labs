from Employee import Employee
from Manager import Manager


class Menu():

    def __init__(self):
        self.action()

    def print_menu(self):
        print("Available operations:")
        print("  Add new employee: 'add'")
        print("  Transfer employee: 'transfer'")
        print("  Fire employee: 'fire'")
        print("  Show employee data: 'show'")
        print("  List all employees: 'list'")
        print("  Quit program: 'q'")

    def action(self):
        quit = False
        while (quit == False):
            self.print_menu()
            operation = input("Enter operation keyword: ")

            if operation == "add":
                employee_type = input(
                    "For adding manager press e \nFor adding manager press m \n")

                if employee_type == "m":
                    self.insert_manager_data()

                elif employee_type == "e":
                    self.insert_emplyee_data()

                else:
                    print("Invalid employee type. Please try again.")

            elif operation == "transfer":
                id = input("Enter employee ID you want to transfer \n")
                employee = Employee.get_employee(id)
                newDep = input(
                    f"Enter new Department you want transfer {employee.first_name} {employee.last_name} To \n")
                employee.transfer(newDep)

            elif operation == "fire":
                id = input("Enter employee ID you want to transfer \n")
                employee = Employee.get_employee(id)
                employee.fire()

            elif operation == "show":
                id = input("Enter employee ID you want to transfer \n")
                employee = Employee.get_employee(id)
                employee.show()

            elif operation == "list":
                # list all employees and their data
                print("\n======== Emplyees List ======")
                Employee.list_employees()

            elif operation == "q":
                quit = True
                print("Bye , We Will Miss You")

            else:
                print("Invalid operation keyword. Please try again.")

            print()

    def insert_manager_data(self):
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        age = int(input("Enter age: "))
        department = input("Enter department: ")
        salary = float(input("Enter salary: "))
        managed_department = input("Enter managed department: ")
        manager = Manager(first_name, last_name, age,
                          department, salary, managed_department)
        manager.insert_to_database()

    def insert_emplyee_data(self):
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        age = int(input("Enter age: "))
        department = input("Enter department: ")
        salary = float(input("Enter salary: "))
        employee = Employee(first_name, last_name,
                            age, department, salary)
        employee.insert_to_database()
