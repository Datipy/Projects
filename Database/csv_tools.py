import csv

# save dictionnary to csv
def dict_to_csv(dict_list, file):
    keys = dict_list[0].keys()

    with open(file, 'w', newline='') as csv_file:
        dict_writer = csv.DictWriter(csv_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(dict_list)
    return "Dictionnary saved to csv successfully"

# return dictionnary from csv_file
def csv_to_dict(csv_file):
    # open csv file and read it
    with open(csv_file) as csv_file:
        reader = csv.reader(csv_file) 
        columns = next(reader) # get csv columns and move reader
        
        # need code for iteration
        dictionnary_list = []
        for rows in reader:
            dictionnary = {columns[0]:rows[0],
                           columns[1]:rows[1],
                           columns[2]:rows[2],
                           }
            dictionnary_list.append(dictionnary)
    csv_file.close()
    return dictionnary_list

if __name__ == '__main__':
    dict_to_csv(arg)