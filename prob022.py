"""
Using names.txt, a 46K text file containing over five-thousand first names, begin by 
sorting it into alphabetical order. Then working out the alphabetical value for each 
name, multiply this value by its alphabetical position in the list to obtain a name 
score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 
3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a 
score of 938 x 53 = 49714.

What is the total of all the name scores in the file?
"""

def score_word(word):
    return sum(ord(letter) - 64 for letter in word)

f = open("Data/prob022.txt", "r")
names = f.readlines()[0].replace("\"", "").split(",")
names.sort()

print sum((i+1) * score_word(names[i]) for i in range(len(names)))