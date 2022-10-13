# ----------------------------------------------------------------------------
# Automatic database connector for sqlite3
# Upgrade in progress :
# => add function to switch technology (Mysql, PostgreSQL, sqlalchemy, others)
# => function to automatically switch between databases
# => execute with multiple queries
# ----------------------------------------------------------------------------

import sqlite3 as sql
import pandas as pd

class My_db_connector():
    """class to connect to different databases
       and execute queries"""
    
    def __init__(self, db_name):
        """connection and cursor object online"""
        
        self.db_name = db_name
        self.connection = sql.connect("{}.db".format(self.db_name))
        self.cursor = self.connection.cursor()
        print("Connection to '{}' database successful".format(self.db_name))
    
    # display all table of database in a dataframe
    def db_show(self):
        query = "SELECT name FROM sqlite_master WHERE type='table';" 
        return self.db_execute_query(query)
    
    # execute query
    def db_execute_query(self, query):
        return pd.read_sql(query, self.connection)
    
    # close connection to database
    def db_close_connection(self):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
        return "Connection to '{}' database closed successful".format(self.db_name)