"""
Author:Callum Egan
20/01/26
Description: lists Excersises q12
"""
num = eval(input("Enter a list of numerators: "))
denum = eval(input("Enter a list of denomonators: "))
smallIndex = 1
for i in range(len(num)):
    if num[i] / denum[i] < num[smallIndex] / denum[smallIndex]:
        smallIndex = i
print(num[smallIndex], "/", denum[smallIndex])