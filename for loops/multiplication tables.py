"""
Author:Callum Egan
10/9/25
Description:Print a multiplication table of a given number
"""
number = int(input("Enter a number: "))
for x in range(13):
    print(f"{number}x{x}={number*x}")
