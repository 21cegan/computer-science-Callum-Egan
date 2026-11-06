"""
Author:Callum Egan
4/9/26
Description:Bubble sort v3
"""
lst = [10,8,6,4,2]
#lst.sort()

for x in range(len(lst)):
    x = len(lst)- x - 1
    sortDone = True
    
    for n in range(x):
        current = lst[n]
        after = lst[n+1]
        
        if current > after:
            lst[n] = after
            lst[n+1] = current
            sortDone = False
        
        print(lst)
    if sortDone:
        break