"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
"""

solutions = []

for a in range(1, 333):
    for b in range(a, 1000 - a):
        for c in range(b, 1000 - b):
            if a**2 + b**2 == c**2:
                #print "Found solution: (%d, %d, %d)" % (a, b, c)
                solutions.append(a+b+c)
                    
print max(set(solutions), key=solutions.count)