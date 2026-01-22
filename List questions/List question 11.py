"""
Author:Callum Egan
20/01/26
Description: lists Excersises q11
"""
str_list = eval(input("Enter a list of strings: "))
str_list.sort(key=len)
print(str_list[-1])

L = eval(input("Enter a list of numbers: "))
num = int(input("Enter a number to add to these: "))
for i in range(len(L)):
    L[i] = L[i] + num
print(L)