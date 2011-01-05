"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
"""

f = ""
for i in xrange(1, 200000):
    f += str(i)
    if len(f) >= 1000000:
        print "Generated f at", i
        break

print int(f[0]) * int(f[9]) * int(f[99]) * int(f[999]) * int(f[9999]) * int(f[99999]) * int(f[999999])