"""
The cube, 41063625 (345^3), can be permuted to produce two other 
cubes: 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the 
smallest cube which has exactly three permutations of its digits which 
are also cube. 

Find the smallest cube for which exactly five permutations of its digits 
are cube.
""" 

from itertools import permutations
CUBEROOT = (1.0 / 3.0)

CUBES = [str(i ** 3) for i in range(1,1000)]

for i in range(500, 1000):
    cube = i ** 3
    
    answers = set(["".join(perm) for perm in permutations(str(cube)) if "".join(perm) in CUBES])
    print i, len(answers)#, answers
    
    if len(answers) == 5:
        print cube, answers
        break