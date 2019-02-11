# Site Statique  
## Projet 1ère année Ynov Informatique Théo DELAS  

### Principe :  
+ Programme permettant de convertir des fichiers au format markdown en html
    + Les fichiers markdown à convertir se trouvent dans le dossier 'fichiers_markdown'  
    + Les fichiers html créés grâce au programme se créeront dans le dossier 'fichiers_html'  

### Utilisation :  
+ Supprimez les fichiers dans les dossiers `fichiers_html`, `fichiers_allemand`, `fichiers_kikoo`  
+ Ouvrir un terminal de commande, et se placer dans le dossier ou se trouve le 'main.py'  
+ Utiliser la ligne de commande `py main.py -i ./fichiers_markdown -o ./fichiers_html` pour convertir les fichiers makdown en des fichiers html   
`-i ./fichiers_markdown` étant le chemin du dossier où se trouvent tous les fichiers markdown à convertir.  
`-o ./fichiers_html` étant le chemin du dossier où l'on veut que les fichiers convertis se créent.  
+ Pour convertir des fichiers html en des fichiers aidant les allemands à les lire, ajouter la commande `-a ./fichiers_allemand`  
`./fichiers_allemand` étant le chemin du dossier où les fichiers convertis en "allemand" se créent.
+ Pour convertir des fichiers html en des fichiers où seront placé des mots aléatoires d'une liste "kikoo", ajouter la commande `-k ./fichiers_kikoo`  
`./fichiers_kikoo` étant le chemin du dossier où les fichiers convertis en "kikoo" se créent.



Collaborators : Durand Antoine, Boisseau Alex

