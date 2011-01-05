"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 
to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, 
multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be 
written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it 
once in your sum.
"""

nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
products = [x*y for x in range(1,50) for y in range(100, 2000) if sorted(list(str(x) + str(y) + str(x*y))) == nums]          
print sum(set(products))