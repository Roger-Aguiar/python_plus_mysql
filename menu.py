# Name:         Roger Silva Santos Aguiar
# Function:     This is the main method to access the other modules
# Initial date: July 22, 2020
# Last update:  July 24, 2020

# Required modules
from Employee import employee_input


class Menu:
    @staticmethod
    def options():
        print("*******************************************************************COMPANY "
              "DATABASE*******************************************************************\n")

        print("1 - EMPLOYEE")
        print("2 - DEPARTMENT")
        print("3 - DEPARTMENT LOCATIONS")
        print("4 - PROJECT")
        print("5 - WORKS ON")
        print("6 - DEPENDENT")
        print("7 - EXIT")

        print("\n******************************************************************************************************************************************************\n")

    def employee_menu(self):
        input_employee = employee_input.EmployeeData()
        input_employee.options()

        option = int(input("\nChoose an option: "))

        while option != 5:
            if option == 1:
                input_employee.insert()
            elif option == 2:
                input_employee.update()
            elif option == 3:
                input_employee.delete()
            elif option == 4:
                input_employee.get_table()

            input_employee.options()
            option = int(input("\nChoose an option: "))


if __name__ == '__main__':
    menu = Menu()

    menu.options()
    option_menu = int(input("Chose an option: "))
    if option_menu == 1:
        menu.employee_menu()
    else:
        print("End program.")
