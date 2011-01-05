"""In the 20x20 grid below, four numbers along a diagonal line have been marked in red.

The product of these numbers is 26 x 63 x 78 x 14 = 1788696.

What is the greatest product of four adjacent numbers in any direction (up, down, left, right, or diagonally) in the 20x20 grid?"""

f = open("Data/prob011.txt", "r")
lines = f.readlines()
table = []
for line in lines:
    table.append([int(x) for x in line.split(" ")])
    
peak = 0
check = 0

#search right
for row in table:
    for i in range(len(row)-3):
        check = row[i] * row[i+1] * row[i+2] * row[i+3]
        if(check > peak):
            peak = check

#search down
for i in range(len(row)):
    for j in range(len(table)-3):
        check = table[j][i] * table[j+1][i] * table[j+2][i] * table[j+3][i]
        if(check > peak):
            peak = check

#search down-right
for i in range(len(row)-3):
    for j in range(len(table)-3):
        check = table[j][i] * table[j+1][i+1] * table[j+2][i+2] * table[j+3][i+3]
        if(check > peak):
            peak = check

#search down-left
for i in range(3, len(row)):
    for j in range(len(table)-3):
        check = table[j][i] * table[j+1][i-1] * table[j+2][i-2] * table[j+3][i-3]
        if(check > peak):
            peak = check

print peak