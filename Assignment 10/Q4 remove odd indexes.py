"""
Author:Callum Egan
23/10/25
Description: Exercise 4
Write a Python program to remove characters that have odd index values in a given 
string.
Example input/output:
User inputs ‘abcdef’ 
Output: ace
"""
string = input("Enter a string: ")
newString = ""
for x in range(len(string)):
    if x % 2 == 0:
        newString += string[x]
print(newString)