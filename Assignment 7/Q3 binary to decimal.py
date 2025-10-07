"""
Author:Callum Egan
7/10/25
Description:  3. Write a program to convert Binary to Decimal
"""
binary = input("Enter a binary number: ")
total = 0
length = len(binary)
for x in binary:
    x = int(x)
    length -= 1
    total += (x * 2**length)
print(total)