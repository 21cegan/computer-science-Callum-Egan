"""
Author:Callum Egan
2/10/25
Description:  Q3. Write a program that takes an integer number and outputs all the even numbers 
starting from 0 to the number
"""
number = input("enter an integer: ")
number = int(number)
n = 0
while n < (number-1):
    n += 2
    print(n)
    