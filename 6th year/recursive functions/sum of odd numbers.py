"""
Author:Callum Egan
5/11/26
Description:sum of odd numbers up to n
"""

def sumOfOdds(n):
    if n%2:
        n -= 1
    if n < 1:
        return 0
    else:
        return 1 + sumOfOdds(n-2)
    
n = int(input("Enter a number to count up to: "))
print(sumOfOdds(n))