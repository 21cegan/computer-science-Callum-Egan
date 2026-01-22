"""
Author:Callum Egan
09/01/26
Description: lists Excersises q1
"""
lst = eval(input("Enter a list: "))
num = int(input("Enter a number: "))
for i in range(len(lst)):
    lst[i] = lst[i] + num
print(lst)