# --------------------------------------------------------------
# Ce script permet de générer les structures de données adaptées
# à l’utilisation de Datipy à partir d’un dossier regroupants
# toutes les sources de données à traiter
# --------------------------------------------------------------

import os
import pandas as pd   
    
# récupère le chemin absolu d’un dossier
def get_folder():
    folder_name = input("enter folder’s path :")
    global folder_path
    folder_path = os.path.abspath(folder_name)

# récupère la liste des fichiers du dossier
def get_files_list():
    files_list = os.listdir(r"{}".format(folder_path))
    return files_list

# formate le nom des fichiers pour le dictionnaire
def get_file_name(file):
    file_name = file.lower().replace(" ", "_")
    file_name = file_name.split(".",1)[0]
    return file_name


# génére les dataframes à partir des fichiers du dossiers
def generate_df(file):
    file_path = r"{}\{}".format(str(os.path.abspath(folder_path)), str(file))
    if "csv" in file:
        return pd.read_csv(file_path)
    elif "xlsx" in file:
        return pd.read_excel(file_path)
    elif "ods" in file:
        return pd.read_excel(file_path, engine="odf")

# génère la liste des dataframes
def generate_list_df():
    global df_list
    df_list = []
    
    # ajout des df à df_list
    for file in get_files_list():
        df_list.append(generate_df(file))  
    
# génère le dictionnaire à partir de la liste des dataframes
def generate_df_dict():
    global df_dict
    df_dict = {}
    
    # ajout couple key-value 
    i = 0
    for file in get_files_list():
        df_dict[get_file_name(file)] = "df_list[{}]".format(i)
        i+=1
    display(df_dict)

if __name__ == '__main__':
    get_folder()
    generate_list_df()
    generate_df_dict()
    print("Tasks completed successfully, df_list and df_dict generated")
    