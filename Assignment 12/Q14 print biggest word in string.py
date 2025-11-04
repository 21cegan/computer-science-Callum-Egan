"""
Author:Callum Egan
04/11/25
Description: Q14 print biggest word in string
"""
string = input("Enter a string of words: ")
words = []

for x in range(0,string.count(" ")):
    words.append(string[:string.index(" ")])
    string = string[string.index(" ")+1:]
    
words.append(string)
words.sort(key=len)
print(words[-1])