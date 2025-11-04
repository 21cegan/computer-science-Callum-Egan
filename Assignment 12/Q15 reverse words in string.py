"""
Author:Callum Egan
04/11/25
Description: Q15 print words in string reversed
"""
string = input("Enter a string of words: ")
newString = ""

for x in range(0,string.count(" ")):
    word = string[string.index(" ")::-1]
    newString +=  word
    string = string[string.index(" ")+1:]
    
newString += " " + string[::-1]
print(newString)