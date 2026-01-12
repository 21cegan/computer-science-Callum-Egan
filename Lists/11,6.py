"""
Author:Callum Egan
09/01/26
Description: lists 11.6
"""

val = eval(input("Enter a list: "))
print("Original list: ",val)
val = val * 2
print("Replicated list:",val)
val.sort()
print("sorted in ascending order: ",val)
val.sort(reverse = True)
print("sorted in descending order: ",val)
