"""By starting at the top of the triangle below and moving to adjacent numbers 
on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below: (in prob018.txt)

NOTE: As there are only 16384 routes, it is possible to solve this problem by 
trying every route. However, Problem 67, is the same challenge with a triangle 
containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)"""

f = open("Data/prob018.txt", "r")
txtrows = f.readlines()
rowlists = {}

for i in range(len(txtrows)):
    rowlists[i] = [int(x) for x in txtrows[i].split(" ")]

#print "Before"
#for row in rowlists.values():
#	print row

for i in xrange(len(txtrows)-1, 0, -1):
	#print "Row", i
	for j in xrange(len(rowlists[i])-1, 0, -1):
		#print "Cell", j
		rowlists[i-1][j-1] += rowlists[i][j-1] if rowlists[i][j-1] > rowlists[i][j] else rowlists[i][j]
	
#print "\nAfter"	
#for row in rowlists.values():
#	print row

print rowlists[0][0]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    