# Name:         Roger Silva Santos Aguiar
# Function:     Database settings.
# Initial date: July 21, 2020
# Last update:  July 24, 2020

# Required module
import mysql.connector


class DatabaseConnection:
    @staticmethod
    def my_connection():
        mydb = mysql.connector.connect\
            (
                host='localhost',
                user='root',
                password='983453069',
                database='COMPANY'
            )

        return mydb