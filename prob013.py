"""Work out the first ten digits of the sum of the following one-hundred 50-digit numbers."""

f = open("Data/prob013.txt", "r")
print str(sum(int(x) for x in f.readlines()))[0:10]


