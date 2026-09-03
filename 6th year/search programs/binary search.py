"""
Author:Callum Egan
3/9/26
Description:Binary search
"""
lst = [2,5,8,12,16,23,38,56,72,91]
wanted = 23

low = 0
high = len(lst)-1
index = -1

while low <= high:
    mid = (low + high)//2
    x = lst[mid]
    if x == wanted:
        index = mid
        break
    elif x > wanted:
        high = mid - 1
    elif x < wanted:
        low = mid + 1

print(index)