"""
Author:Callum Egan
09/01/26
Description: lists Excersises q6
"""
lst = eval(input("Enter a list: "))
num = int(input("Enter a number to search the list for: "))
if num not in lst:
    print(num,"not found in this list")
else:
    for i in range(len(lst)):
        if lst[i] == num:
            print(num, "found at place",i+1)
