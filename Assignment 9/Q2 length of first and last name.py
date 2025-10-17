"""
Author:Callum Egan
17/10/25
Description:  Q2. Ask the user to enter their first name and then their surname. Join them together 
with a space between and then display their full name and the length of their full name
"""
firstName = input("Enter your first name: ")
secondName = input("Enter your second name: ")
print(f"Your name is {firstName} {secondName} \nthere are {len(firstName)+len(secondName)} characters in your name")