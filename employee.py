# Name:         Roger Silva Santos Aguiar
# Function:     This module implements all the functionalities of EMPLOYEE table
# Initial date: July 21, 2020
# Last update:  July 23, 2020

# Required modules
import database_service


class Employee:
    database = database_service.DatabaseService()

    def select(self):
        sql = 'SELECT * FROM EMPLOYEE'
        table = self.database.select(sql)
        return table

    def select_by_id(self, id_row):
        sql = 'SELECT * FROM EMPLOYEE WHERE Ssn = %s'
        ssn = (id_row,)
        table = self.database.select_by_id(sql, ssn)
        return table

    def insert(self, values):
        sql = "INSERT INTO EMPLOYEE " \
              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        self.database.insert(sql, values)

    def update(self, values):
        sql = "UPDATE EMPLOYEE SET Fname = %s, Minit = %s, Lname = %s, Bdate = %s, Address = %s, Sex = %s, " \
              "Salary = %s " \
              "WHERE Ssn = %s "

        self.database.update(sql, values)

    def delete(self, ssn_employee):
        sql = "DELETE FROM EMPLOYEE WHERE Ssn = %s"
        ssn = (ssn_employee,)
        self.database.delete(sql, ssn)

    def display_options(self):
        print("\n*************************************************************Menu"
              "*************************************************************")
        print("1 - Show employees")
        print("2 - Insert a new employee")
        print("3 - Update Employee")
        print("4 - Delete Employee")
        print("5 - Exit")
