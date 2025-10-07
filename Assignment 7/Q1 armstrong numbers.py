"""
Author:Callum Egan
7/10/25
Description:  1. Write a program to check if a number is an Armstrong number. An Armstrong 
number is a number equal to the sum of the cube of it’s digits
"""
total = 0
number = input("Enter a number: ")
for x in number:
    x = int(x)
    total += x**3
if str(total) == number:
    print(number,"is an armstrong number")
else:
    print(number, "is not an armstrong number")
