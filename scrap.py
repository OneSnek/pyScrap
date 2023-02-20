#import random
import random

#"""
wide = 5
tall = 5
grid = []
cell = "*"

for ylen in range(tall):
    row = []
    for xlen in range(wide):
        row.append(cell)
    grid.append(row)

#grid modifications
grid[2][3] = "O"
grid[0][0] = "X"

#print the grid
for i in range(len(grid)):
    print(grid[i])

#function time:
def grille(xdim,ydim):
    tab = []
    cell = "*"
    for i in range(ydim):
        line = []
        for  i in range (xdim):
            line.append(cell)
        tab.append(line)
    return tab

tableau = grille(9,9)
for i in range(len(tableau)):
    print(tableau[i])

#definir largeur et longueur de mon tableau 2D
#creer fonction qui generert renvoie un tab 2D rempli de cellules mortes ou vivantes
#creer une fonction qui itere sur chaque cell du tab (parcours)
#creer fonction qui examine les voisins
#def une funct qui permet de: utiliser fonct de verif dans la fonction d'iteration + renvoie une copie

#Execution
#gener un tab + assigner une variable
#une boucle infinie (While True:) qui affiche le tab de la fonct precedente
#avec comme parametre le tableau, l'assigner a une variable "tableauCopy"
# definir que le tableau est egal a tableau copy

#end code