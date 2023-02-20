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
print("\n")



#FUNCTION TIME:
def grille(xdim,ydim):
    tab = []
    cell = "--"
    for i in range(ydim):
        line = []
        for  i in range (xdim):
            line.append(cell)
        tab.append(line)
    return tab
#example
print("example de tableau avec appel de fonction grille")
tableau = grille(9,9)
tableau[0][0] = "00"
tableau[1][4] = "14"
tableau[8][8] = "88"
for i in range(len(tableau)):
    print(tableau[i])
print("\n")



#FONCTION ITERATIVE
def iter(tab):
    dimy = len(tab) # x dimension (horizontal)
    dimx = len(tab[0]) # y dimension (vertical)
    print ("tableau is " + str(dimy) + " tall(Y) and " + str(dimx) + " wide(X):")
    for i in range (dimy):
        for j in range (dimx):
            tab[i][j] = str(i)+str(j)
    for i in range(dimy):
        print(tab[i])
    return
#example
print("example appel fonction iterative")
iter(tableau)

#final print


#definir largeur et longueur de mon tableau 2D? check
#creer fonction qui generert renvoie un tab 2D rempli de cellules mortes ou vivantes? check
#creer une fonction qui itere sur chaque cell du tab (parcours)
#creer fonction qui examine les voisins
#def une funct qui permet de: utiliser fonct de verif dans la fonction d'iteration + renvoie une copie

#Execution:
#gener un tab + assigner une variable
#une boucle infinie (While True:) qui affiche le tab de la fonct precedente
#avec comme parametre le tableau, l'assigner a une variable "tableauCopy"
# definir que le tableau est egal a tableau copy.

#end code