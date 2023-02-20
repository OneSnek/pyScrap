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



#FONCTION (grille) DE CREATION DE TABLEAU (tab):
def grille(xdim,ydim):
    tab = []
    cell = "--"
    for i in range(ydim):
        line = []
        for  i in range (xdim):
            line.append(cell)
        tab.append(line)
    return tab
#example/exec
print("example de tableau avec appel de fonction grille")
tableau = grille(9,9)
tableau[0][0] = "00"
tableau[1][4] = "14"
tableau[8][8] = "88"
for i in range(len(tableau)):
    print(tableau[i])
print("\n")



#FONCTION ITERATIVE (iter)
def iter(tab):
    dimy = len(tab) # y dimension (vertical)
    dimx = len(tab[0]) # x dimension (horizontal)
    print ("tableau is " + str(dimy) + " tall(Y) and " + str(dimx) + " wide(X):")
    for i in range (dimy):
        for j in range (dimx):
            tab[i][j] = str(i)+str(j)
    for i in range(dimy):
        print(tab[i])
    return
#example/exec
print("example appel fonction iterative")
iter(tableau)
print("\n")


#FONCTION QUI EXAMINE LES VOISINS (check)
def check(tabl, y, x):
    v = 0 #nombre de voisins vivants
    if y != 0: #il y a de la place pour un voisin vers le nord
        if tabl[y-1][x] != "--":
            v=v+1
    if y < len(tabl): #il y a de la place pour un voisin vers le sud
        if tabl[y+1][x] != "--":
            v=v+1
    if x < len(tabl[0]): #il y a de la place pour un voisin vers l'est
        if tabl[y][x+1] != "--":
            v=v+1
    if x != 0: #il y a de la place pour un voisin vers l'ouest
        if tabl[y][x-1] != "--":
            v=v+1
    if x!=0 and y!=0: #il y a de la place pour un voisin vers le nord-ouest
        if tabl[y-1][x-1] != "--":
            v=v+1
    if x < len(tabl[0]) and y!=0: #il y a de la place pour un voisin vers le nord-est
        if tabl[y-1][x+1] != "--":
            v=v+1
    if x < len(tabl[0]) and y < len(tabl): #il y a de la place pour un voisin vers le sud-est
        if tabl[y+1][x+1] != "--":
            v=v+1
    if x != 0 and y < len(tabl): #il y a de la place pour un voisin vers le sud-ouest
        if tabl[y+1][x-1] != "--":
            v=v+1
    return v #nombre total de voisins
#example/exec
print(check(tableau,1,4))
print("\n")

#FONCTION = ITERATION + DO CHECK + RETURN COPY ("the next step" = next)
def next(tab):
    dimy = len(tab) # y dimension (vertical)
    dimx = len(tab[0]) # x dimension (horizontal)
    print ("tableau is " + str(dimy) + " tall(Y) and " + str(dimx) + " wide(X):")
    copy = tab #copie du tableau a ecrire dessus
    for i in range (dimy):
        for j in range (dimx):
            life = random.randint(0,1) #randomize life of cells
            if life == 0:
                tab[i][j] = str(i)+":"+str(j) #cell is alive
            else:
                tab[i][j] = "---" #cell is dead
    for i in range(dimy):
        print(tab[i])
    return
#example/exec
next(tableau)
print (random.randint(0,1))

#definir largeur et longueur de mon tableau.
#creer fonction qui generert renvoie un tab 2D rempli de cellules mortes ou vivantes.
#creer une fonction qui itere sur chaque cell du tab (parcours)
#creer fonction qui examine les voisins
#def une funct qui permet de: utiliser fonct de verif dans la fonction d'iteration + renvoie une copie

#Execution:
#gener un tab + assigner une variable
#une boucle infinie (While True:) qui affiche le tab de la fonct precedente
#avec comme parametre le tableau, l'assigner a une variable "tableauCopy"
# definir que le tableau est egal a tableau copy.

#end code