"""
Author:Callum Egan
5/11/26
Description:sum of digits in non negative num
"""

def sumOfDigits(n):
    if not n:
        return 0
    else:
        return int(n[0]) + sumOfDigits(n[1:])

number = input("Enter a non negative integer: ")
print(sumOfDigits(number))