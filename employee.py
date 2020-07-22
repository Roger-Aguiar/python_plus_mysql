# Name:         Roger Silva Santos Aguiar
# Function:     This module implements all the functionalities of EMPLOYEE table
# Initial date: July 21, 2020
# Last update:  July 22, 2020

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
        sql = "UPDATE EMPLOYEE SET Fname = %s, Minit = %s, Lname = %s, Bdate = %s, Address = %s, Sex = %s, " \
              "Salary = %s " \
              "WHERE Ssn = %s "

        f_name = 'Tom'
        m_init = 'S'
        l_name = 'Aguiar'
        b_date = '2019-11-01'
        address = '630 Japurá, Centro, MG'
        sex = 'M'
        salary = 20000
        ssn = '987321654'

        values = (f_name, m_init, l_name, b_date, address, sex, salary, ssn)

        self.employees.execute(sql, values)
        self.mydb.commit()

        print("The row was successfully updated!")

    def delete_employee(self):
        sql = "DELETE FROM EMPLOYEE WHERE Ssn = %s"
        ssn = ('987321654',)

        print("Are you sure that you want to delete this row? \n")
        print("1 - Yes")
        print("2 - No")

        operation_option = int(input("Choose an option: "))

        if operation_option == 1:
            self.employees.execute(sql, ssn)
            self.mydb.commit()
            print("The row was successfully deleted!")
        else:
            print("End operation.")

    def display_options(self):
        print("\n*************************************************************Menu"
              "*************************************************************")
        print("1 - Show employees")
        print("2 - Insert a new employee")
        print("3 - Update Employee")
        print("4 - Delete Employee")
        print("5 - Exit")


if __name__ == '__main__':
    employee = Employee()
    employee.display_options()

    option = int(input("\nChoose an option: "))

    while option != 5:
        if option == 1:
            employee.show_employees()
        elif option == 2:
            employee.insert_employee()
        elif option == 3:
            employee.update_employee()
        elif option == 4:
            employee.delete_employee()

        employee.display_options()
        option = int(input("\nChoose an option: "))