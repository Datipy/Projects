import csv

""" functions to list dictionaries 
    for csv saving
    """

# tables_dict to save to tables.csv
def define_table_list(table_dict):
    to_csv = []
    
    # for each table
    for key, values in table_dict.items():
        # for each table’s attribut
        for value in values:
            template = {"table_name": key, 
                        "column_name": value,
                        "data_type": df[value].dtypes
                       }
            # add template to list
            to_csv.append(template)
    return to_csv

# references_dict to save to references.csv
def define_reference_list(ref_dict):
    to_csv = []

    # for each table
    for key, values in ref_dict.items():
        # for each table’s reference
        for value in values:
            template = {"table": key, 
                        "referenced_by": value,
                       }
            # add template to list
            to_csv.append(template)
    return to_csv


""" functions to :
    - transfer dictionary to csv
    - get dictionary from csv
    """

# save dictionnary to csv
def dict_to_csv(dict_list, file):
    keys = dict_list[0].keys()

    with open(file, 'w', newline='') as csv_file:
        dict_writer = csv.DictWriter(csv_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(dict_list)
    return "Dictionary saved to csv successfully"

# return dictionnary from csv_file
def csv_to_dict(csv_file):
    # open csv file and read it
    with open(csv_file) as csv_file:
        reader = csv.reader(csv_file) 
        columns = next(reader) # get csv columns and move reader
        
        # loop to load dict
        dictionaries_list = []
        for rows in reader:
            # add each row to list
            dictionary = {}
            for i in range(len(columns)):
                dictionary[columns[i]] = rows[i]
            dictionaries_list.append(dictionary)
    csv_file.close()
    return dictionaries_list