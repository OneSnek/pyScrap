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
#"""


#end code