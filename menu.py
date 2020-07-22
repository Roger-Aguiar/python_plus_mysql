# Name:         Roger Silva Santos Aguiar
# Function:     This is the main method to access the other modules
# Initial date: July 22, 2020
# Last update:  July 22, 2020

# Required modules
import employee


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


if __name__ == '__main__':
    menu = Menu()

    menu.options()

    option = int(input("Choose an option: "))