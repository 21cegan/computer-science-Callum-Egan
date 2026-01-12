"""
Author:Callum Egan
12/01/26
Description: lists 11.12
"""
lst = eval(input("Enter list: "))
ln = len(lst)
mx = max(lst)
ind = lst.index(mx)
if ind <= (ln/2):
    print("The maximum element",mx,"lies in the first half.")
else:
    print("The maximum element",mx,"lies in the second half.")