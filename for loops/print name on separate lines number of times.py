"""
Author:Callum Egan
10/9/25
Description:Ask the user to enter their name and a number. Display each letter of their name 
on a separate line and repeat this for the number of times they entered
"""
name = input("enter your name: ")
number = int(input("enter a number: "))

for x in range(number):
    for l in name:
        print(l)