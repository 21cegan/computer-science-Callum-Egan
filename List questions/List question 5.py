"""
Author:Callum Egan
09/01/26
Description: lists Excersises q5
"""
lst = eval(input("Enter a list of strings: "))
for i in range(len(lst)):
    lst[i] = lst[i][1:]
print(lst)