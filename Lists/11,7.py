"""
Author:Callum Egan
09/01/26
Description: lists 11.7
"""
lst = eval(input("Enter a list: "))
length = len(lst)
min_ele = lst[0]
min_index = 0
for i in range(1,length) :
    if lst[i] < min_ele:
        min_index = i
        min_ele = lst[i]
print("Given list is:",lst)
print("The minimum element of the given list is: ")
print(min_ele, "at index",min_index)
