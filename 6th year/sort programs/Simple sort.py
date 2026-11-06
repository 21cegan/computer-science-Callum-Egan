"""
Author:Callum Egan
9/9/26
Description:simple sort
"""

unsortedList = [3,5,7,2,1]

sortedList = []

while unsortedList:

    smallestIndex = 0
    
    for x in range(len(unsortedList)):
        if unsortedList[x] < unsortedList[smallestIndex]:
            smallestIndex = x
            
    sortedList.append(unsortedList.pop(smallestIndex))
    
    print(sortedList)
        