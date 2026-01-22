"""
Author:Callum Egan
22/01/26
Description: lists Excersises q14
"""
lst = eval(input("Enter a list: "))
usedValues = []
duplicateValues = []
for i in lst:
    if i in usedValues:
        duplicateValues.append(i)
    else:
        usedValues.append(i)
newList = usedValues+duplicateValues
print(newList)