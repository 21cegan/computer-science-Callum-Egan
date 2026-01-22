"""
Author:Callum Egan
20/01/26
Description: lists Excersises q10
"""

n = int(input("Enter the term of the fibonacci sequence: "))
sequence = [0,1]
for i in range(n-1):
    sequence.append(sequence[-1]+sequence[-2])
print(sequence[-1])