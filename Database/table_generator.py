# ----------------------------------------------------
# SQLalchemy Tables generator using csv_file
# free user from manually creating tables
# ----------------------------------------------------

from sqlalchemy import Table, Column, DateTime, Integer, Float, String, MetaData
from csv_tools import csv_to_dict

# define MetaData()
def metadata_online():
    global metadata_obj
    metadata_obj = MetaData()
    print("metadata_obj is online")

# create all required tables in metadata_obj
def create_all_tables(dict_list):
    # get set of unique table
    table_set = set([list(dict.values())[0] for dict in dict_list])

    # create tables for table in set
    for table in table_set:
        Table(table, 
              metadata_obj, 
              Column(table+"_id", 
                     Integer, primary_key = True))
    print("Tables creation successful")

# append Column to Table in metadata_obj
def table_add_column(values, sql_type):   
    # define Column
    column_obj = Column(values[1], sql_type)
    # get table to append column
    table = metadata_obj.tables[values[0]]
    return table.append_column(column_obj)

# append all Columns for each attributs selected
def add_all_columns(dict_list):
    # dict to translate data_type into sql_type
    sql_type = {"int64": Integer,
                  "float64": Float,
                  "object": String,
                  "datetime64[ns]": DateTime}
    
    # iterate for rows in csv_file
    for dictionnary in dict_list:
        values = list(dictionnary.values())
        sql_type = sql_type[values[2]]
        table_add_column(values, sql_type)
    print("Columns added to Tables successfully", "\n")

def display_metadata_tables(metadata_obj):
    print("metadata_obj :", "\n")
        
    for value in metadata_obj.tables.values():
        for column in value.columns.keys():
            print("Table : ;", value, 
                  "Column : ;", column) # add data_type
                                        # change params
                                        # to match method

if __name__ == '__main__':
    dict_list = csv_to_dict("tables.csv") # load tables
    metadata_online()
    create_all_tables(dict_list)
    add_all_columns(dict_list)
    display_metadata_tables(metadata_obj)