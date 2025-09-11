"""
Author:Callum Egan
10/9/25
Description:Ask the user to enter their name and their number. Display their name the given 
number of times.
"""

name = input("Enter your name: ")
number = int(input("enter a number: "))

for x in range(number):
    print(name)