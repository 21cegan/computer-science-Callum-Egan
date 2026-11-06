"""
Author:Callum Egan
4/9/26
Description:Bubble sort v1
"""
lst = [10,8,6,4,2]

for x in range(len(lst)):
    
    for n in range(len(lst)-1):
        current = lst[n]
        after = lst[n+1]
        
        if current > after:
            lst[n] = after
            lst[n+1] = current
        
        print(lst)