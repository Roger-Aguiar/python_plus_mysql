# Name:         Roger Silva Santos Aguiar
# Function:     This module gets the employee data from the user.
# Initial date: July 22,2020
# Last update:  July 24,2020

# Required modules
from Employee import employee


class EmployeeData:
    data = employee.Employee()

    def __init__(self):
        self.table = []

    def insert(self):
        f_name = input("Enter the first name: ")
        m_init = input("Enter the middle name: ")
        l_name = input("Enter the last name: ")
        ssn = input("Enter the ssn:")
        b_date = input("Enter the birth date: ")
        address = input("Enter the full address: ")
        sex = input("Enter the genre: ")
        salary = float(input("Enter the salary: "))

        values = (f_name, m_init, l_name, ssn, b_date, address, sex, salary)

        self.data.insert(values)

    def delete(self):
        self.get_table()

        ssn = input("Please, enter the employee's ssn that you want to delete from the database: ")
        self.data.delete(ssn)

    def update(self):
        self.get_table()

        ssn = input("Please, enter the employee's ssn that you want to update: ")
        row = self.data.select_by_id(ssn)

        print(row)
        f_name = row[0]
        m_init = row[1]
        l_name = row[2]
        b_date = str(row[4])
        address = row[5]
        sex = row[6]
        salary = float(row[7])

        print("\n1 - Fname | 2 - Minit | 3 - Lname | 4 - Bdate | 5 - Address | 6 - Sex | 7 - Salary | 8 - Cancel")

        field = int(input("\nChoose what field that you want to update or type 8 to cancel this operation: "))

        while field != 8:
            if field == 1:
                f_name = input("Enter the fist name: ")
            elif field == 2:
                m_init = input("Enter the Minit: ")
            elif field == 3:
                l_name = input("Enter the last name: ")
            elif field == 4:
                b_date = input("Enter the birth date: ")
            elif field == 5:
                address = input("Enter the address: ")
            elif field == 6:
                sex = input("Enter the genre: ")
            elif field == 7:
                salary = float(input("Enter the salary: "))
            else:
                print("Operation was canceled by the user.")

            print("\n1 - Fname | 2 - Minit | 3 - Lname | 4 - Bdate | 5 - Address | 6 - Sex | 7 - Salary | 8 - Cancel")
            field = int(input("\nChoose what field that you want to update or type 8 to cancel this operation: "))

        values = (f_name, m_init, l_name, b_date, address, sex, salary, ssn)
        self.data.update(values)

    def get_table(self):
        self.table = self.data.select()
        self.show_table(self.table)

    def show_table(self, table):
        print("EMPLOYEES\n")

        print("-----------------------------------------------------------------------------------------------------------------------------")
        print("FName           | Minit | Lname          | Ssn       | Bdate      | Address                       | Sex  | Salary           |")
        print("-----------------------------------------------------------------------------------------------------------------------------")
        for row in table:
            f_name = " " * (15 - len(row[0]))
            f_name = row[0] + f_name + "|"
            m_init = " " + row[1] + "     | "
            l_name = " " * (15 - len(row[2]))
            l_name = row[2] + l_name + "| "
            ssn = row[3] + " | "
            b_date = str(row[4]) + " | "
            address = " " * (30 - len(row[5]))
            address = row[5] + address + "| "
            sex = row[6] + "    | "
            salary = str(row[7])
            salary = "$ " + salary + (" " * (15 - len(salary))) + "|"

            current_row = "|" + f_name + m_init + l_name + ssn + b_date + address + sex + salary

            print(current_row)
        print("-----------------------------------------------------------------------------------------------------------------------------")

    def options(self):
        print("\n***********************************************************************EMPLOYEE**********************************************************************")
        print("1 - Insert employee")
        print("2 - Update employee")
        print("3 - Delete employee")
        print("4 - Show employes")
        print("5 - Exit")
        print("*******************************************************************************************************************************************************")

