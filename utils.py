"""
Utility methods for use solving Euler problems
"""
from math import sqrt

def fibonacci_term(n):
    """Returns the nth 0-based term of the Fibonacci sequence"""
    return int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))

def fibonacci_sequence(max):
    """Returns the fibonacci sequence up to max"""
    term = fibonacci_term(0)
    f = []
    i = 1
    while term < max:
        f.append(term)
        term = fibonacci_term(i)
        i += 1
    return f

def fibonacci_generator():
    f0, f1 = 0, 1
    while True:
        yield f0
        f0, f1 = f1, f0+f1
    
def seive_of_eratosthenes(n):
    """Produces a list of prime numbers <= n"""
    sieve = [ True for i in range(n+1) ]
    def markOff(pv):
        for i in range(pv+pv, n+1, pv):
            sieve[i] = False
    markOff(2)
    for i in range(3, n+1):
        if sieve[i]:
            markOff(i)
    return [ i for i in range(2, n+1) if sieve[i] ]
    
def triangle(n):
    """Returns the nth triangle number"""
    return (n * (n + 1)) / 2

def pentagonal(n):
    """Returns the nth pentagonal number"""
    return (n * ((3 * n) - 1)) / 2
    
def factors(n):
    """Returns a sorted set of factors of n"""
    factors = []
    for x in range(1, int(sqrt(n)+1)):
        if (n % x) == 0:
            factors += [x, n/x]
    
    return sorted(set(factors))
    
def number_as_string(x):
    """Returns a number <= 20999 as an English string"""
    
    numnames = {1 : "one", 2 : "two", 3 : "three", 4 : "four", 5 : "five", 6 : "six", 7 : "seven", 8 : "eight", 9 : "nine",
            10 : "ten", 11 : "eleven", 12 : "twelve", 13 : "thirteen", 14 : "fourteen", 15 : "fifteen", 16 : "sixteen",
            17 : "seventeen", 18 : "eighteen", 19 : "nineteen", 20 : "twenty", 30 : "thirty", 40 : "forty", 50 : "fifty", 
            60 : "sixty", 70 : "seventy", 80 : "eighty", 90 : "ninety"}
    
    numparts = []
    needAnd = (x > 100) and (x % 100)
    if x >= 1000:
        numparts.append(numnames[x/1000])
        numparts.append("thousand")
        x %= 1000
    
    if x >= 100:
        numparts.append(numnames[x/100])
        numparts.append("hundred")
        x %= 100
    
    if needAnd:
        numparts.append("and")
    
    if 11 <= x <= 19:
        numparts.append(numnames[x])
    else:
        if x >= 10:
            numparts.append(numnames[(x/10)*10])
            x %= 10

        if x > 0:
            numparts.append(numnames[x])
            
    return " ".join(numparts)