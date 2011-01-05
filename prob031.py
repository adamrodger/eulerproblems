"""
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

1x£1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p

How many different ways can £2 be made using any number of coins?
"""

count = 0

for a in xrange(200, -1, -200):
    for b in xrange(a, -1, -100):
        for c in xrange(b, -1, -50):
            for d in xrange(c, -1, -20):
                for e in xrange(d, -1, -10):
                    for f in xrange(e, -1, -5):
                        for g in xrange(f, -1, -2):
                            count += 1
print count