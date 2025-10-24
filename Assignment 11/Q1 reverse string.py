"""
Author:Callum Egan
23/10/25
Description:  Q1. Write a program to reverse a string using:
• A for loop
• A while loop
• Slicing
"""

string = input("Enter a string: ")
reverseString = ""
for x in string:
    reverseString = x + reverseString
print(reverseString)

count = 0
reverseString2 = ""
while count < len(string):
    reverseString2 = string[count] + reverseString2
    count += 1
print(reverseString2)

print(string[::-1])
    