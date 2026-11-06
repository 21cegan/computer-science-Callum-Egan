"""
Author:Callum Egan
23/9/26
Description:insertion sort
"""

lst = [11,7,14,19,12]
print(lst)

for i in range(1,len(lst)):
    marker = lst[i]
    
    for j in range(i-1,-1,-1):
        if lst[j] > marker:
            lst[j],lst[i] = lst[i],lst[j]
            i = j
            print(lst)