"""
Author:Callum Egan
12/01/26
Description: lists 11.8
"""
lst = eval(input("Enter list: "))
length = len(lst)
mean = sum = 0
for i in range(0,length):
    sum += lst[i]
mean = sum / length
print("Given list is:",lst)
print("The mean of the given list is:",mean)