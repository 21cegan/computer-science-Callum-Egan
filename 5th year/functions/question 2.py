"""
Author:Callum Egan
30/04/26
Description: ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both
words begin with same letter
"""
def animal_crackers(a):
    firstChar = a.index(" ") + 1
    if a[0] == a[firstChar]:
        return True
    else:
        return False
    
    
print(animal_crackers("hello there"))