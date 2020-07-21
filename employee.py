# Name:         Roger Silva Santos Aguiar
# Function:     This module implements all the functionalities of EMPLOYEE table
# Initial date: July 21, 2020
# Last update:  July 21, 2020

# Required modules
import database_config


class Employee:
    def __init__(self):
        self.mydb = database_config.DatabaseConnection.my_connection()
        self.employees = self.mydb.cursor()

    def show_employees(self):
        sql = 'SELECT * FROM EMPLOYEE'
        self.employees.execute(sql)
        employee_table = self.employees.fetchall()

        for row in employee_table:
            print(row)

    def insert_employee(self):
        sql = "INSERT INTO EMPLOYEE " \
              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        f_name = 'Tom'
        m_init = 'S'
        l_name = 'Aguiar'
        ssn = '987321654'
        b_date = '2019-11-01'
        address = '222 Piauí, Tupanuára, MG'
        sex = 'M'
        salary = 10000

        values = (f_name, m_init, l_name, ssn, b_date, address, sex, salary)

        self.employees.execute(sql, values)
        self.mydb.commit()

        print("Operation has been completed.\n")

    def update_employee(self):
        pass

    def delete_employee(self):
        pass

    def employee_menu(self):
        pass


if __name__ == '__main__':
    employee = Employee()

    print("1 - Show employees")
    print("2 - Insert a new employee")
    print("3 - Exit")

    option = int(input("\nChoose an option: "))

    if option == 1:
        employee.show_employees()
    elif option == 2:
        employee.insert_employee()
    elif option == 3:
        print("End program.")