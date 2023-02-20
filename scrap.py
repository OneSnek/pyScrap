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


#end code