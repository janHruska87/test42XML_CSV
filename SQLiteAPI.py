

import sqlite3 as sqlite3

class db:

    def __init__(self):
        self.dbPath = ""

    def connectToDB(self, dbPath):
        "self.dbPath = ""jdbc:sqlite:"" + dbPath"


    def createTable(self,dbPath,tableName,headers):
        """"Funkce pro vytvoreni tabulky, vstupni atributy jsou tableName a seznam sloupcu / datovych typu"""

        """Prvni sloupec je vzdycky pouzit jako primary key, ostatni dle typu uvedeno v header"""
        sql = "CREATE TABLE " + tableName + " ("
        for e in headers:
            sql = sql + e[0] + " " + e[1] + " , "
        sql = sql.rstrip(" , ")
        sql = sql + ");"
        try:
            self.sqliteConnection = sqlite3.connect(dbPath)
            sqlite_create_table_query = sql

            cursor = self.sqliteConnection.cursor()
            print("Successfully Connected to SQLite")
            cursor.execute(sqlite_create_table_query)
            self.sqliteConnection.commit()
            print("SQLite table created")

            cursor.close()

        except sqlite3.Error as error:
            print("Error while creating a sqlite table", error)
        finally:
            if self.sqliteConnection:
                self.sqliteConnection.close()
                print("sqlite connection is closed")