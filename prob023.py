""" A perfect number is a number for which the sum of its proper
divisors is exactly equal to the number. For example, the sum of the
proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means
that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is
less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
smallest number that can be written as the sum of two abundant numbers
is 24. By mathematical analysis, it can be shown that all integers
greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis
even though it is known that the greatest number that cannot be
expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as
the sum of two abundant numbers.
"""

from utils import factors

abundant = [i for i in xrange(12, 28124) if i*2 < sum(factors(i))] #note: factors returns the number original number as well so we need to multiply by 2
abundant = [x for x in abundant if x < 14062]

sums = []
for x in range(len(abundant)):
    for y in range(x):
        if abundant[x] + abundant[y] not in sums:
            sums.append(abundant[x] + abundant[y])

#sums = [abundant[x] + abundant[y] for x in range(len(abundant)) for y in range(x, len(abundant)) if abundant[x] + abundant[y] < 28124]
print sum(x for x in range(28124) if not (x in sums))

