"""
Author:Callum Egan
5/11/26
Description:sum of number in list
"""



def sumOfList(n):
    if len(n) == 0:
        return 0
    
    else:
        return n[0] +sumOfList(n[1:])

numList = [1,3,2,5,6,2,1]
print(sumOfList(numList))
