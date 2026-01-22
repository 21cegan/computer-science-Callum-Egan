"""
Author:Callum Egan
09/01/26
Description: lists Excersises q4
"""
lst = eval(input("Enter a list containing numbers between 1 and 12: "))
for i in range(len(lst)):
    if lst[i] > 10:
        lst[i] = 10
print(lst)
