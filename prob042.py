"""
The nth term of the sequence of triangle numbers is given by, tn = (n * (n + 1)) / 2; so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values 
we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a 
triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common 
English words, how many are triangle words?
"""

from utils import triangle
triangles = [triangle(n) for n in range(1,20)]

f = open("Data/words.txt", "r")
words = f.readlines()[0].replace("\"", "").split(",")

print len([word for word in words if sum(ord(c) - 64 for c in word) in triangles])