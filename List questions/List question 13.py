"""
Author:Callum Egan
22/01/26
Description: lists Excersises q13
"""
lst = eval(input("Enter a list of numbers: "))
rangeMin = int(input("Enter the first index to search from: "))
rangeMax = int(input("Enter the last index to search to: "))

newList = lst[rangeMin:rangeMax]
newList.sort()
print(newList[0], "is the smallest value and", newList[-1],"is the largest.")