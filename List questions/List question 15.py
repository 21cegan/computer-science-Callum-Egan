"""
Author:Callum Egan
22/01/26
Description: lists Excersises q15
"""
lst1 = eval(input("Enter the a list: "))
lst2 = eval(input("Enter the a list: "))
for i in range(len(lst1)):
    if lst1[i] != lst2[i]:
        print("Lists differ at index",i)
        break