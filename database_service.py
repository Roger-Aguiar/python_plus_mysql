# Name:         Roger Silva Santos Aguiar
# Function:     This module implements all the operations with the database
# Initial date: July 22, 2020
# Last update:  July 23, 2020

# Required modules
import database_config


class DatabaseService:
    def __init__(self):
        self.mydb = database_config.DatabaseConnection.my_connection()
        self.database = self.mydb.cursor()

    def select(self, sql):
        self.database.execute(sql)
        table = self.database.fetchall()

        return table

    def select_by_id(self, sql, id_row):
        self.database.execute(sql, id_row)
        table = self.database.fetchone()

        return table

    def insert(self, sql, values):
        self.database.execute(sql, values)
        self.mydb.commit()

        print("Operation has been completed.\n")

    def delete(self, sql, id_table):
        print("Are you sure that you want to delete this row? \n")
        print("1 - Yes")
        print("2 - No")

        operation_option = int(input("Choose an option: "))

        if operation_option == 1:
            self.database.execute(sql, id_table)
            self.mydb.commit()
            print("The row was successfully deleted!")
        else:
            print("End operation.")

    def update(self, sql, values):
        self.database.execute(sql, values)
        self.mydb.commit()

        print("The row was successfully updated!")