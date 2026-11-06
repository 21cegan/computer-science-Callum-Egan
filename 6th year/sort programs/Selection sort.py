"""
Author:Callum Egan
9/9/26
Description:selection sort
"""

List = [3,5,7,2,1]
marker = 0


for x in range(len(List)-1):

    smallestIndex = marker
    
    for x in range(marker+1, len(List)):
        if List[x] < List[smallestIndex]:
            smallestIndex = x
            
    
    if smallestIndex != marker:
        List[marker], List[smallestIndex] = List[smallestIndex], List[marker]
    
    marker += 1
    print(List)