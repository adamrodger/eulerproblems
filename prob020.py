"""n! means n x (n - 1) x ... x 3 x 2 x 1

Find the sum of the digits in the number 100!"""

from math import factorial
print sum(int(x) for x in str(factorial(100)))

