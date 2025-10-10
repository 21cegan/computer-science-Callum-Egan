"""
Author:Callum Egan
10/10/25
Description:  Q19. Print every number between 1 and n divisible by m,
and say whether or not that number divisible by m is even or odd
"""

n = int(input("Input an integer for the max value checked: "))
m = int(input("Input another integer to check if values are divided by: "))

for x in range(1,n):
    if x % m == 0 and x % 2 == 0:
        print(x, "is divisible by", m,"and is even")
    if x % m == 0 and x % 2 == 1:
        print(x, "is divisible by", m,"and is odd")
