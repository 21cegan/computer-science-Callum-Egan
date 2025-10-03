"""
Author:Callum Egan
3/10/25
Description:  Q6. Write a program which takes in a numbers from the user. It should continue taking 
in numbers until the total of all the numbers entered is greater than 50.
"""
total = 0
while total < 50:
    num = input("Enter a number: ")
    num = float(num)
    total += num
    print(total)