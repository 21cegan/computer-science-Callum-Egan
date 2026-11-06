"""
Author:Callum Egan
15/10/26
Description: Frequency of words in a sentence
"""
sentence = input("Enter a sentence: ")

wordList = sentence.split(" ")

frequencyDict = {}

for x in wordList:
    x = x.capitalize()
    if x in frequencyDict:
        frequencyDict[x] += 1
    else:
        frequencyDict[x] = 1
print("Word     Frequency")
for key,value in frequencyDict.items():
    print(key, "->",value)