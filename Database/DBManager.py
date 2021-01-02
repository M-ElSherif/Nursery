import os
import sqlite3

"""
Profiles Table
userid  name    age     height      weight
"""


class DBManager:
    package_dir = os.path.abspath(os.path.dirname(__file__))
    db_dir = os.path.join(package_dir, "Nursery.sqlite")
    SQLITE_DB = db_dir

    # TODO: add a class method here that creates the table and commits it to the database

    @classmethod
    def create_connection(self, dbName=SQLITE_DB):
        try:
            self.sql_connection = sqlite3.connect(dbName)
            return self.sql_connection
        except Exception as e:
            print(e)

    @classmethod
    def close_connection(self):
        self.sql_connection.close()
