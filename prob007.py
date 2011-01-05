"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6^(th) prime is 13.

What is the 10001st prime number?
"""

from utils import seive_of_eratosthenes
print seive_of_eratosthenes(110000)[10000]