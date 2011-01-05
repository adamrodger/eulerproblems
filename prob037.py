"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits 
from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to 
left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from utils import seive_of_eratosthenes
primes = []
answers = []

for prime in seive_of_eratosthenes(1000000):
    temp = str(prime)
    if "0" not in temp and "2" not in temp[1:-1] and "4" not in temp and "6" not in temp and "8" not in temp:
        primes.append(temp)

def is_truncatable(s, left=True):
    while(len(s)):
        if s not in primes:
            return False
            
        s = s[1:] if left else s[:-1]
    else:
        return True

for prime in primes:
    if is_truncatable(prime, True) and is_truncatable(prime, False):
        answers.append(prime)

print sum(int(a) for a in answers) - 17

#748317