# Name:         Roger Silva Santos Aguiar
# Function:     This module gets the employee data from the user.
# Initial date: July 22,2020
# Last update:  July 22,2020

# Required modules
import employee


class EmployeeData:
    data = employee.Employee()

    def insert_new_employee(self):
        f_name = input("Enter the first name: ")
        m_init = input("Enter the middle name: ")
        l_name = input("Enter the last name: ")
        ssn = input("Enter the ssn:")
        b_date = input("Enter the birth date: ")
        address = input("Enter the full address: ")
        sex = input("Enter the genre: ")
        salary = float(input("Enter the salary: "))

        values = (f_name, m_init, l_name, ssn, b_date, address, sex, salary)

        self.data.insert_employee(values)


if __name__ == '__main__':
    input_employee = EmployeeData()

    input_employee.insert_new_employee()
