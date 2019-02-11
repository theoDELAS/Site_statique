import markdown2
import os
import re
import argparse
import random

# pour convertir les liens html
link_patterns = [(re.compile(r'((([A-Za-z]{3,9}:(?:\/\/)?)(?:[\-;:&=\+\$,\w]+@)?[A-Za-z0-9\.\-]+(:[0-9]+)?|(?:www\.|[\-;:&=\+\$,\w]+@)[A-Za-z0-9\.\-]+)((?:\/[\+~%\/\.\w\-_]*)?\??(?:[\-\+=&;%@\.\w_]*)#?(?:[\.\!\/\\\w]*))?)'),r'\1')]
# création des arguments de argparse
parser = argparse.ArgumentParser(description = "Transforme un fichier Markdown en un fichier Html")
parser.add_argument("-i", "--input", type = str, required = True, metavar = "", help = "Le chemin du dossier contenant les fichiers Markdown à convertir en HTML")
parser.add_argument("-o", "--output", type = str, required = True,metavar = "", help = "Le chemin du dossier où seront mis les fichiers HTML générés pour le site statique")
parser.add_argument("-t", "--template", type = str, metavar = "", help = "Dossier contenant des modèles de page web à compléter")
parser.add_argument("-k", "--kikoo", type = str, required = False,metavar = "", help = "Ajoute dans le texte des « kikoo », « lol », « mdr », « ptdr » ou qui répète des lettres comme dans Hellllo, et autres déformations du français")
parser.add_argument("-a", "--achtung", type = str, required = False, metavar = "", help = "Aide les allemands à lire nos blogs français")

args = parser.parse_args()
# dossier d'entrée contenant les fichiers markdown
dossier_md = args.input
# dossier de sortie où seront créer des fichiers html
dossier_html = args.output
# dossier de sortie où seront créer des fichiers html avec des mots de kikoo
dossier_kikoo = args.kikoo
# dossier de sortie ou seront créer des fichiers html pour aider la lisibilité des allemands
dossier_allemand = args.achtung
dossier_temp = args.template

# liste chaque fichier dans le dossier
liste = os.listdir(dossier_md)

#fonction permettant de convertir le code markdown en html
def convertir_html(dossier_md, dossier_html):
    compteur = 0
    # permet de lire le contenu de chaque fichier du dossier
    for fichier in liste:
        with open(f'{dossier_md}/{fichier}', "r") as file:
            convert_html = markdown2.markdown(file.read(), extras = ["link-patterns"] ,link_patterns = link_patterns)
            fichier_html = open(f'{dossier_html}/index{compteur}.html', "w")
            fichier_html.write(convert_html)
            fichier_html.close()
            compteur += 1

# liste des fiichiers dans le dossier html
liste_html = os.listdir(dossier_html)

# Fonction pour convertir le code en un fichier plus lisible pour les allemands
def convertir_achtung(dossier_html, dossier_allemand):
    compteur = 0
    # permet de lire le contenu de chaque fichier du dossier
    for fichier in liste_html:
        fichier_html = open(f'{dossier_html}/{fichier}', "r") # ouvre chaque fichier dans le dossier d'entrée
        fichier_allemand = open(f'{dossier_allemand}/index_allemand{compteur}.html', "w") # ouvre un nouveau fichier dans le dossier de sortie
        # remplacement des lettres
        for ligne in fichier_html:
            for lettre in ligne:
                if lettre != "s" and lettre != "c" and lettre != "q":
                    fichier_allemand.write(lettre)
                elif lettre == "s":
                   fichier_allemand.write(lettre.replace("s", "z"))
                elif lettre == "c":
                    fichier_allemand.write(lettre.replace("c", "z"))
                elif lettre == "q":
                    fichier_allemand.write(lettre.replace("q", "k"))
        compteur += 1

# Fonction pour convertir le code avec des "kikoo, lol, mdr ..."
def convertir_kikoo(dossier_html, dossier_kikoo):
    mots_kikoo = ["mdr", "lol", "ptdr", "kikoo", "xptdr"]
    compteur = 0
    # permet de lire le contenu de chaque fichier du dossier
    for fichier in liste_html:
        fichier_html = open(f'{dossier_html}/{fichier}', "r")
        fichier_kikoo = open(f'{dossier_kikoo}/index_kikoo{compteur}.html', "w")
        for ligne in fichier_html:
            fichier_kikoo.write(ligne + random.choice(mots_kikoo))
        compteur += 1

# Appel des fonctions
convertir_html(dossier_md, dossier_html)

if dossier_allemand:
    convertir_achtung(dossier_html, dossier_allemand)

if dossier_kikoo:
    convertir_kikoo(dossier_html, dossier_kikoo)
