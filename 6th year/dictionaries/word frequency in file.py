"""
Author:Callum Egan
15/10/26
Description: Frequency of words in a file
"""

f = open("book.txt","r")
book = f.read()
wordList = book.split(+)


frequencyDict = {}

for x in wordList:
    if x in frequencyDict:
        frequencyDict[x] += 1
    else:
        frequencyDict[x] = 1

def sv(x):
    return x[1]

sortedList = sorted(frequencyDict.items(),key = sv,reverse = True)
print("Word     Frequency")
for key,value in sortedList[:10]:
    print(key, "->",value)