"""
Author:Callum Egan
12/01/26
Description: lists 11.15
"""
lst1 = eval(input("Enter list: "))
lst2 = eval(input("Enter list: "))
mx1 = max(lst1)
mx2 = max(lst2)

if mx1 >= mx2:
    print(mx1,"The maximum value is in list1 at index",lst1.index(mx1))
else:
    print(mx2,"The maximum value is in list2 at index",lst2.index(mx2))
