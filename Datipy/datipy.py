# -----------------------------------------------------------
# Datipy est un ensemble d’outils pour faciliter la lecture 
# des tables avant de procéder au nettoyage puis aux analyses.
#
# Actuellement les classes utilisent un dictionnaire contenant
# les tables. Le code est en train d’être actualisé pour
# travailler avec un dictionnaire reférençant les tables
# -----------------------------------------------------------

# librairie pour avoir les décorateurs intéractifs
import ipywidgets as widgets
from ipywidgets import interact, interact_manual

# basic data kit
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# librairie pour un format statistique des tables
import researchpy as rp


class Display():
    """ Classe primaire pour afficher simplement 
        une table selon les attributs séléctionnés. """

    def __init__(self, dictionnary):
        self.dict = dictionnary
        
        # récupération des attributs de 
        self.keys = widgets.Dropdown(options=list(self.dict)) 
        self.attribut_widget = widgets.SelectMultiple(
            options=list(self.dict[(self.keys.value)].columns))

    def update_attribut(self, *args):
        self.attribut_widget.options = self.dict[(self.keys.value)].columns

    def show_query(self, selected_df, attribut):
        df = self.dict[selected_df]
        return df[list(attribut)]

    def interact(self):
        self.keys.observe(self.update_attribut, 'value')
        interact_manual(self.show_query, selected_df=self.keys,
                        attribut=self.attribut_widget)

        
class Datipy(Display):

    def __init__(self, dictionnary):
        Display.__init__(self, dictionnary)
        self.method = ["Datipy", "info", "describe", "codebook"]

    def update_attribut(self, *args):
        Display.update_attribut(self, *args)

    def show_query(self, selected_df, attribut, method):
        df = self.dict[selected_df]
        if method == "Datipy":
            return df.loc[:, attribut]
        elif method == "info":
            return df.info()
        elif method == "describe":
            return df.loc[:, attribut].describe()
        elif method == "codebook":
            return rp.codebook(df.loc[:, attribut])

    def interact(self):
        self.keys.observe(self.update_attribut, 'value')
        interact_manual(self.show_query, selected_df=self.keys, attribut=self.attribut_widget,
                        method=self.method)
        

class Scribe(Display):

    def __init__(self, dictionnary):
        Display.__init__(self, dictionnary)
        self.filtre_widget = widgets.SelectMultiple(
            options=list(self.dict[(self.keys.value)].columns))
        self.pipe = ["", ".isna()", ".isin([{}])", ".str.contains({})",
                     ".str.contains(""|"".join([{}]))"]

    def update_attribut(self, *args):
        Display.update_attribut(self, *args)
        self.filtre_widget.options = self.dict[(self.keys.value)].columns

    def show_query(self, selected_key, attribut, filtre, pipe, text=widgets.Text(), bool=["", "~"]):
        df = self.dict[selected_key]
        if pipe != "":
            pipe = pipe.format(str(text))
        if text != "":
            return eval("df.loc[:,{}][{}df{}{}]".format(list(attribut), bool, list(filtre), pipe))
        else:
            return df.loc[:, list(attribut)]

    def interact(self):
        self.keys.observe(self.update_attribut, 'value')
        interact_manual(self.show_query, selected_key=self.keys, attribut=self.attribut_widget,
                        filtre=self.filtre_widget,
                        pipe=self.pipe)


