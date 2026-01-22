"""
Author:Callum Egan
19/01/26
Description: lists Excersises q8
"""
L = eval(input("Enter the first list: "))
M = eval(input("Enter another list of the same size: "))

if len(L) != len(M):
    print("Different lengths of lists")
    exit()
N = []
for i in range(len(L)):
    N.append(L[i]+M[i])
print(N)