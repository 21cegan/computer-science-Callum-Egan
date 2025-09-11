"""
Author:Callum Egan
10/9/25
Description:Print the sum of all the odd numbers from 1 to a given numbe
"""
number = int(input("enter a number: "))
total = 0
for x in range(number+1):
    if x % 2 ==1:
        total += x
print(total)