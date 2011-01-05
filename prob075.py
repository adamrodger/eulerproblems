"""
It turns out that 12 cm is the smallest length of wire that can be bent 
to form an integer sided right angle triangle in exactly one way, but 
there are many more examples. 

12 cm: (3,4,5) 
24 cm: (6,8,10) 
30 cm: (5,12,13) 
36 cm: (9,12,15) 
40 cm: (8,15,17) 
48 cm: (12,16,20) 

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an 
integer sided right angle triangle, and other lengths allow more than 
one solution to be found; for example, using 120 cm it is possible to 
form exactly three different integer sided right angle triangles. 

120 cm: (30,40,50), (20,48,52), (24,45,51) 

Given that L is the length of the wire, for how many values of L <=
1,500,000 can exactly one integer sided right angle triangle be formed? 

Note: This problem has been changed recently, please check that you are 
using the right parameters. 
"""

solutions = {}

def pythagorean_triplet(n, m):
    return tuple(sorted([m*m - n*n, 2 * m * n, m*m + n*n]))

if __name__ == "__main__":
    for n in range(1, 899):
        for m in range(n + 1, 900):
            a, b, c = pythagorean_triplet(n, m)
            if a<b and b<c and a + b + c <= 1500000:
                if not (a+b+c in solutions):
                    solutions[a+b+c] = [(a, b, c)]
                elif not (a,b,c) in solutions[a+b+c]:
                    solutions[a+b+c].append((a, b, c))
                    
                #work out the imprimitives
                x = a+b+c
                for f in xrange(2, 100001):
                    t = x * f
                    if t > 1500000:
                        break
                    else:
                        if not (t in solutions):
                            solutions[t] = [(a*f, b*f, c*f)]
                        elif not (a*f,b*f,c*f) in solutions[t]:
                            solutions[t].append((a*f, b*f, c*f))

    result = [k for k in solutions if len(solutions[k]) == 1]

    print solutions[12]
    print solutions[24]
    print solutions[30]
    print solutions[36]
    print solutions[40]
    print solutions[48]
    print solutions[120]

    #print result
    print len(result)
        