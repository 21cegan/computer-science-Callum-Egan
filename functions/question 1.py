"""
Author:Callum Egan
30/04/26
Description: 1 LESSER OF TWO EVENS: Write a function that returns the lesser of two given
numbers if both numbers are even, but returns the greater if one or both numbers are
odd
"""
def lesser_of_two_evens(a,b):
    if a > b:
        big = a
        small = b
    else:
        small = a
        big = b
    if a % 2 or b % 2: #even%2 = false, odd % 2 = true
        return big
    else:
        return small
print(lesser_of_two_evens(61,406))