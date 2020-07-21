# Name:         Roger Silva Santos Aguiar
# Function:     This module implements all the functionalities of EMPLOYEE table
# Initial date: July 21, 2020
# Last update:  July 21, 2020

# Required modules
import database_config


class Employee:
    def __init__(self):
        self.mydb = database_config.DatabaseConnection.my_connection()

    def show_employees(self):
        employees = self.mydb.cursor()
        sql = 'SELECT * FROM EMPLOYEE'
        employees.execute(sql)
        employee_table = employees.fetchall()

        for row in employee_table:
            print(row)

    def insert_employee(self):
        pass

    def update_employee(self):
        pass

    def delete_employee(self):
        pass

    def employee_menu(self):
        pass


employee = Employee()
employee.show_employees()