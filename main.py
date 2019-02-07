import markdown2
import os
import re
import argparse

link_patterns = [(re.compile(r'((([A-Za-z]{3,9}:(?:\/\/)?)(?:[\-;:&=\+\$,\w]+@)?[A-Za-z0-9\.\-]+(:[0-9]+)?|(?:www\.|[\-;:&=\+\$,\w]+@)[A-Za-z0-9\.\-]+)((?:\/[\+~%\/\.\w\-_]*)?\??(?:[\-\+=&;%@\.\w_]*)#?(?:[\.\!\/\\\w]*))?)'),r'\1')]

parser = argparse.ArgumentParser(description = "Transforme un fichier Markdown en un fichier Html")
parser.add_argument("-i", "--input", type = str, required = True, metavar = "", help = "Le chemin du dossier contenant les fichiers Markdown à convertir en HTML")
parser.add_argument("-o", "--output", type = str, required = True,metavar = "", help = "Le chemin du dossier où seront mis les fichiers HTML générés pour le site statique")
parser.add_argument("-t", "--template", type = str, metavar = "", help = "Dossier contenant des modèles de page web à compléter")
parser.add_argument("-k", "--kikoo", type = str, metavar = "", help = "Ajoute dans le texte des « kikoo », « lol », « mdr », « ptdr » ou qui répète des lettres comme dans Hellllo, et autres déformations du français")
parser.add_argument("-a", "--achtung", type = str, metavar = "", help = "Aide les allemands à lire nos blogs français")

args = parser.parse_args()

dossier_md = args.input
dossier_html = args.output
dossier_temp = args.template
kikoolol = args.kikoo
allemand = args.achtung

# liste chaque fichier dans le dossier
liste = os.listdir(dossier_md)

def convertir(dossier_md, dossier_html):
    compteur = 0
    # permet de lire le contenu de chaque fichier du dossier
    for fichier in liste:
        with open(f'{dossier_md}/{fichier}', "r") as file:
            convert_html = markdown2.markdown(file.read(), extras = ["link-patterns"] ,link_patterns = link_patterns)
            fichier_html = open(f'{dossier_html}/index{compteur}.html', "w")
            fichier_html.write(convert_html)
            fichier_html.close()
            compteur += 1

convertir(dossier_md, dossier_html)

def achtung():
    print("ok")

if allemand == True:
    achtung()
