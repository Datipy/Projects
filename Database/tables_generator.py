# -------------------------------------------
# SQLalchemy Tables generator using csv_file
# free user from manually creating tables 
# -------------------------------------------

from sqlalchemy import Table, Column, DateTime, Integer, Float, String, ForeignKey, MetaData
from csv_tools import csv_to_dict


""" functions to set up metadata"""

# define MetaData()
def metadata_online():
    global metadata_obj
    metadata_obj = MetaData()
    print("metadata_obj is online")

    
""" functions to create all tables"""    
    
# get_table set of unique table
def get_dict_set(dict_list):
    return set([list(dict.values())[0] for dict in dict_list])

# Warning : Tables are not defined 
# only passed to metadata_obj
def create_all_tables(dict_list):
    # get set of tables
    table_set = get_dict_set(dict_list)
    # create tables for table in set
    for table in table_set:
        Table(table, 
              metadata_obj, 
              Column("id", 
                     Integer, 
                     primary_key = True))
    print("Tables creation successful")

    
""" functions to add all columns to tables """ 

# get table from metadata_obj
def get_table(table_name):
    return metadata_obj.tables[table_name]

# append Column to Table in metadata_obj
def table_add_column(sql_type, table_name, column_name, data_type):   
    # define Column
    column_obj = Column(column_name, sql_type)
    # get table to append column
    table = get_table(table_name)
    # append column
    return table.append_column(column_obj)

# append all Columns for each attributs selected
def add_all_columns(dict_list):
    # dict to translate data_type into sql_type
    sql_type_dict = {"int64": Integer,
                  "float64": Float,
                  "object": String,
                  "datetime64[ns]": DateTime}
    
    # iterate for rows in csv_file
    for dictionary in dict_list:
        # get data_type from dictionary
        data_type = str(dictionary["data_type"])
        # get sql_type from sql_type_dict
        sql_type = sql_type_dict[data_type]
        # add all columns
        table_add_column(sql_type, **dictionary)
    print("Columns added to Tables successfully", "\n")

    
""" functions to add foreign_keys """    

# define foreign_key Column
def define_foreign_column(referenced_by):
    return Column(referenced_by+"_id",
                  Integer,
                  ForeignKey(referenced_by+".id")
                 )

# add Foreign_key to table
def add_fkey_to_table(table, referenced_by):
    fkey = define_foreign_column(referenced_by)
    return get_table(table).append_column(fkey)

# add all references to table
def add_references(ref_dict_list):
    # unpack ref_dict_list
    for dictionary in ref_dict_list:
        add_fkey_to_table(**dictionary)

                
""" functions to display final result"""                
                
# display all tables in metadata_obj
def display_metadata_tables(metadata_obj):
    print("metadata_obj :", "\n")
        
    for value in metadata_obj.tables.values():
        for column in value.columns.keys():
            print("Table :", value, 
                  "; Column :", column) # add data_type
                                        # change params
                                        # to match sql method
                    
if __name__ == '__main__':
    # load tables
    tables_dict_list = csv_to_dict("tables.csv")
    # load references
    ref_dict_list = csv_to_dict("references.csv")
    metadata_online()
    create_all_tables(tables_dict_list)
    add_all_columns(tables_dict_list)
    add_references(ref_dict_list)
    display_metadata_tables(metadata_obj)