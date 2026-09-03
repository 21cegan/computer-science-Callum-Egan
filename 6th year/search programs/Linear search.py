"""
Author:Callum Egan
2/9/26
Description:Linear search
"""

lst = [1,2,3,4,5,6,7,8,9]
want = 20
index = -1

for x in range(len(lst)):
    if lst[x-1] == want:
        index = x-1
        break
print(index)