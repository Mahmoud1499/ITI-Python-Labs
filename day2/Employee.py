import mysql.connector

from db_connection import get_database_connection


class Employee:
    __all_employees = []

    def __init__(self, first_name, last_name, age, department, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.department = department
        self.salary = salary
        self.__all_employees = self.__get_employees()
        self.__class__.__all_employees.append(self)
        # self.insert_to_database()

    def insert_to_database(self):
        try:
            db = get_database_connection()
            cursor = db.cursor()
            sql = "INSERT INTO employee (first_name, last_name, age, department, salary , managed_department) VALUES (%s, %s, %s, %s, %s,'NONE')"
            val = (self.first_name, self.last_name,
                   self.age, self.department, self.salary)
            cursor.execute(sql, val)
            db.commit()
            print("Record inserted successfully \n")
        except mysql.connector.Error as error:
            print(f"Failed to insert record into MySQL table: {error}")
        finally:
            cursor.close()
            db.close()

    def transfer(self, new_department):
        self.department = new_department
        self.__update_database('department', new_department)

    def __update_database(self, column, new_value):
        try:
            db = get_database_connection()
            cursor = db.cursor()
            sql = f"UPDATE employee SET {column} = %s WHERE first_name = %s AND last_name = %s AND age= %s"
            val = (new_value, self.first_name, self.last_name, self.age)
            cursor.execute(sql, val)
            db.commit()
            print(f"{cursor.rowcount} record(s) updated successfully \n")
        except mysql.connector.Error as error:
            print(f"Failed to update record in MySQL table: {error}")
            cursor.close()
            db.close()

    def fire(self):
        self.__class__.__all_employees.remove(self)
        self.__delete_from_database()

    def __delete_from_database(self):
        try:
            db = get_database_connection()
            cursor = db.cursor()
            sql = "DELETE FROM employee WHERE first_name = %s AND last_name = %s"
            val = (self.first_name, self.last_name)
            cursor.execute(sql, val)
            db.commit()
            print(f"{cursor.rowcount} record(s) deleted successfully \n")
        except mysql.connector.Error as error:
            print(f"Failed to delete record from MySQL table: {error}")
        finally:
            cursor.close()
            db.close()

    def show(self):
        print(
            f"Name: {self.first_name} {self.last_name}\nAge: {self.age}\nDepartment: {self.department}\nSalary: {self.salary}\n")

    @classmethod
    def list_employees(cls):
        db = get_database_connection()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM employee")
        rows = cursor.fetchall()
        for row in rows:
            print(
                f"ID: {row[0]}\nName: {row[1]} {row[2]}\nAge: {row[3]}\nDepartment: {row[4]}\nSalary: {row[5]}\nManagered Department: {row[6]}\n ")
        db.close()
        return rows

    @classmethod
    def __get_employees(cls):
        db = get_database_connection()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM employee")
        rows = cursor.fetchall()
        db.close()
        return rows

    @classmethod
    def get_employee(cls, id):
        db = get_database_connection()
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM employee WHERE id= {id} ")
        rows = cursor.fetchone()
        id, first_name, last_name, age, department, salary, managed_department = rows
        # print(cursor)
        return cls(first_name, last_name, age, department, salary)
