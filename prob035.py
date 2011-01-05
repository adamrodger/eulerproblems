"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from utils import seive_of_eratosthenes
from itertools import permutations

primes = [str(i) for i in seive_of_eratosthenes(1000000) if not str(i).count("2") and not str(i).count("4") and not str(i).count("5") and not str(i).count("6") and not str(i).count("8") and not str(i).count("0")]
print "Found", len(primes), "primes"
count = 2 # 2 and 5 are circular, but filtered out above

for i, prime in enumerate(primes):
    if i % 100 == 0:
        print "Checking prime", i
    rotate = prime
    
    #rotate the string
    for j in range(len(prime)):
        if rotate not in primes:
            break
        rotate = rotate[1:] + rotate[0]
        #print "Rotated to", rotate
    else:
        print prime, "is good"
        count += 1

print count