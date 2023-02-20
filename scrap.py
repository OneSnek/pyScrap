#import random
import random

#define the cells via class
"""
class Cell(object):
    position = (int,int)
    life = bool
def __init__(xy, yesno):
    self.position = xy
    self.life = yesno 
"""
#definir largeur et longueur de mon tableau 2D
#creer fonction qui generert renvoie un tab 2D rempli de cellules mortes ou vivantes
#creer une fonction qui itere sur chaque cell du tab (parcours)
#creer fonction qui examine les voisins

#create the Grid
"""
wide = 10
tall = 10

#generer tab 2D avec fonction
def grid(wide, tall):
    tab = [[0]*wide]*tall
    tab[0][1] = 1
    for i in tab:
        print(i)
    return
#execute said function
grid (9, 9)
"""

#"""
wide = 10
tall = 10
grid = []
row = []
cell = "*"
for i in range(wide):
    row.append(cell)
for i in range(tall):
    grid.append(row)

#grid modifications
grid[2][3] = "X"
grid[5][3] = "V"

#print the grid
for i in range(len(grid)):
    print(grid[i])
#"""
#end code