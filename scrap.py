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


#create the Grid
wide = 10
tall = 10
grid = []
row = []
cell = "*"
for i in range(wide):
    row.append(cell)
for i in range(tall):
    grid.append(row)

#print the grid
for i in range(len(grid)):
    print(grid[i])

#end code