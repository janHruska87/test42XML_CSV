

import sqlite3 as sqlite3

class db:

    def __init__(self):
        self.dbPath = ""

    def connectToDB(self, dbPath):
        "self.dbPath = ""jdbc:sqlite:"" + dbPath"


    def createTable(self,dbPath,tableName,headers):
        try:
            self.sqliteConnection = sqlite3.connect(dbPath)
            sqlite_create_table_query = '''CREATE TABLE SqliteDb_developers (
                                        id INTEGER PRIMARY KEY,
                                        name TEXT NOT NULL,
                                        email text NOT NULL UNIQUE,
                                        joining_date datetime,
                                        salary REAL NOT NULL);'''

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