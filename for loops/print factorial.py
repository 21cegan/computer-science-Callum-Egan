"""
Author:Callum Egan
1/9/25
Description:print the factorial of a non-negative integer
"""
number = int(input("enter a non negative integer: "))
total = 1
for x in range(number):
    total *= (x+1)
print(total)