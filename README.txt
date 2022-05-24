**************************************************
****                    IA+                *******
****  TP4 : Classificateur Bayesien Naïf   *******
****                Elise NOGA             *******
**************************************************

Fichier classBayNaif.py 

Plusieurs inputs sont nécessaires :

1.	Nom du fichier contenant les données d'entraînement
Ici : iris.csv

2.	Type de délimiteurs dans ce fichier
Ici : ;

3.	Nom, dans l'ordre d'apparition dans les données, des catégories
Ici :
Iris Setosa
Iris Versicolour
Iris Virginica

4.	Nom du fichier contenant les données de test
Ici : iris_test.csv

5.	Type de délimiteurs dans ce fichier
Ici : ;

Deux graphes s'affichent : 
- Les gaussiennes pour chaque catégories et pour chaque attribut des données
- Le nombre d'erreur faites en fonction de la catégorie lors des tests

S'affichent également en print : 
La catégorie estimée et la catégorie réelle pour chaque donnée de la base de test.




Difficultés rencontrées : 

Les sigmas ne sont pas exactement aux valeurs attendues. Les formules données étant respectées à la lettre,
il est envisageable que des questions d'arrondis ou de valeurs trop petites rentrent en jeu.
