"""
Author:Callum Egan
19/01/26
Description: lists Excersises q9
"""
lst = eval(input("Enter a list: "))

digit = lst.pop(-1)
lst.insert(0,digit)
print(lst)