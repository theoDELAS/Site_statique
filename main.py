import markdown2
import os
import re
import argparse

link_patterns = [(re.compile(r'((([A-Za-z]{3,9}:(?:\/\/)?)(?:[\-;:&=\+\$,\w]+@)?[A-Za-z0-9\.\-]+(:[0-9]+)?|(?:www\.|[\-;:&=\+\$,\w]+@)[A-Za-z0-9\.\-]+)((?:\/[\+~%\/\.\w\-_]*)?\??(?:[\-\+=&;%@\.\w_]*)#?(?:[\.\!\/\\\w]*))?)'),r'\1')]

parser = argparse.ArgumentParser(description = "Transforme un fichier Markdown en un fichier Html")
parser.add_argument("-i", "--input", type = str, metavar = "", help = "Le chemin du dossier contenant les fichiers Markdown à transformer")
parser.add_argument("-o", "--output", type = str, metavar = "", help = "Le chemin du dossier où seront mis les fichiers Html générés pour le site statique")
parser.add_argument("-t", "--template", type = str, metavar = "", help = "Dossier contenant des modèles de page web à compléter")
parser.add_argument("-k", "--kikoo", type = str, metavar = "", help = "Ajoute dans le texte des « kikoo », « lol », « mdr », « ptdr » ou qui répète des lettres comme dans Hellllo, et autres déformations du français")
parser.add_argument("-a", "--achtung", type = str, metavar = "", help = "Aide les allemands à lire nos blogs français")

args = parser.parse_args()

dossier_md = args.input
dossier_html = args.output
dossier_temp = args.template

# ouvre le fichier donné
ouvrir_md = open(dossier_md, "r")

# converti du md en html
convert_html = markdown2.markdown(ouvrir_md.read())
print(convert_html)

# liste chaque fichier dans le dossier
liste = os.listdir(dossier_md)

# permet de lire le contenu de chaque fichier du dossier
for fichier in liste:
    with open(f'{dossier_md}/{fichier}', "r") as file:
        toto = file.readlines()
    print(toto)
