# Dossier des projets de formation

Ce dossier comprend les projets les plus complets de formation sous jupyter et les outils ojets "Datipy" que j’ai commencé à écrire pour accompagner et faciliter mon travail d’analyse de données. Il sera complété par d’autres projets divers.

- Ipywidgets :

  - Les projets sont réalisés sous jupyter et utilisent la librairie "ipywidgets" pour avoir des fonctions intéractives afin de naviguer plaus facilement dans les données et les graphiques ou objets créés à partir de celles-ci

  - La librairie s’installe normalement en debut de chaque notobook où elle est utilisée avec la commande : !conda install ipywidgets
  - Si toutes fois un problème surgissait, la librairie s’installe depuis "Anaconda prompt" avec la commande suivante : pip install ipywidgets

  - La librairie se touve à cette adresse pour plus de détails du fonctionnement des décorateurs intéractifs : 
    - https://ipywidgets.readthedocs.io/en/stable/
 
- Datipy (OOP):

  - Datipy est un ensemble de classes fait afin de travailler plus facilement avec des tables pour diverses tâches : visualisation, recherche, édition, etc.
  - Le fichier python Datipy.py a été écrit avec ses différentes classes en début de formation et doit être réécrit et repensé avec un meilleur code.
  - L’ajout des classes en questions sur ce git est en cours.
  
  - Les différentes classes s’utilisent de la manière suivante par exemple pour appeler "Display":
    - name_object = Display(dictionnary_name)
    - name_object.interact()
    
  - Liste des classes de Datipy :
    - Datipy : affiche les tables selon leurs attributs sélectionnés. Toutes les classes suivantes héritent de Datipy et conserve cette fonctionnalité.
    - Display : L’affichage fait appel à d’autres librairie pour faciliter la lecture statistique des tables (ex : researchpy)
    - Scribe : Permet de filtrer l’afffichage avec des sélections simples ou multiples.
    - Outsider (à repenser) : Permet de traiter les outliers visuellement avec un tableau de commandes intéractives.


- Crédits :
  À l’ensemble des personnes qui ont rédigé les librairies et leur documentation respective que j’utilise pour developper mes compétences en programmation.
  À l’ensemble des proches et mentors qui m’accompagnent de par leurs conseils et leur soutien.
