"""
Author:Callum Egan
5/11/26
Description:sum of reciprocals for first n ints
"""
def sumOfRecipricals(n):
    if not n:
        return 0
    else:
        return 1/n + sumOfRecipricals(n-1)

n = int(input("Enter a number to count up to: "))
print(sumOfRecipricals(n))