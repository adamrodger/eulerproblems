"""Starting in the top left corner of a 22 grid, there are 6 routes (without backtracking) to the bottom right corner.

How many routes are there through a 20x20 grid?"""

from math import factorial

def path_count(x, y):
    return factorial(x + y) / (factorial(x) * factorial(y))
    
print path_count(20, 20)