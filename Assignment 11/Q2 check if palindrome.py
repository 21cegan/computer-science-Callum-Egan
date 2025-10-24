"""
Author:Callum Egan
23/10/25
Description: Q2. Write a program to check if a string is a palindrome. A palindrome is a word or string 
that reads the same backwards and forwards. For example: racecar; rotator
"""
string = input("Enter a string: ")
if string == string[::-1]:
    print(string,"is a palindrome")
else:
    print(string, "is not a palindrome")