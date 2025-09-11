"""
Author:Callum Egan
10/9/25
Description: Print all the even numbers within the given range
"""
number = int(input("enter a max number: "))
for x in range(number+1):
    if x % 2 == 0:
        print(x)