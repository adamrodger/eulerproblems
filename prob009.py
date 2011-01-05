"""
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

for c in xrange(1, 1000):
    #print "Checking a", a
    for b in xrange(1, c):
        for a in xrange(1, b):
            if (a*a) + (b*b) == (c*c):
                if a + b + c == 1000:
                    print a, b, c
                    raise SystemExit