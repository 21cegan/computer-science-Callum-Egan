"""
Author:Callum Egan
15/10/26
Description: Frequency of words or letters in a sentence
"""
sentence = input("Enter a sentence: ")

while True:
    choice = input("Do you want to count (letters) or (words): ")
    choice = choice.upper()
    if choice == "LETTERS":
        wordList = sentence.replace(" ","")
        break
    elif choice == "WORDS":
        wordList = sentence.split(" ")
        break
    else:
        print("Invalid Input")

frequencyDict = {}

for x in wordList:
    x = x.capitalize()
    if x in frequencyDict:
        frequencyDict[x] += 1
    else:
        frequencyDict[x] = 1
if choice == "LETTERS":
    print("Letter     Frequency")
else:
    print("Word     Frequency")
for key,value in frequencyDict.items():
    print(key, "->",value)