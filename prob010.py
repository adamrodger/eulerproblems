"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from utils import seive_of_eratosthenes
print sum(seive_of_eratosthenes(2000000))
