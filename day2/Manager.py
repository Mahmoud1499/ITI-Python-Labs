import mysql.connector
from db_connection import get_database_connection
from Employee import Employee


class Manager(Employee):
    def __init__(self, first_name, last_name, age, department, salary, managed_department):
        super().__init__(first_name, last_name, age, department, salary)
        self.managed_department = managed_department

    def show(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")
        print(f"Managed Department: {self.managed_department}")
        print("Salary: Confidential")
        print()

    def insert_to_database(self):
        try:
            db = get_database_connection()
            cursor = db.cursor()
            sql = "INSERT INTO employee (first_name, last_name, age, department, salary , managed_department) VALUES (%s, %s, %s, %s, %s,%s)"
            val = (self.first_name, self.last_name,
                   self.age, self.department, self.salary, self.managed_department)
            cursor.execute(sql, val)
            db.commit()
            print("Record inserted successfully \n")
        except mysql.connector.Error as error:
            print(f"Failed to insert record into MySQL table: {error}")
        finally:
            cursor.close()
            db.close()
