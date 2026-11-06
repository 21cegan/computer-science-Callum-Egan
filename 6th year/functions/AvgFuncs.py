"""
Author:Callum Egan
24/9/26
Description:Function Practice
"""
def mean(numList):
    total = 0
    for x in numList:
        total += x
    
    mean = total/ len(numList)
    return mean

def median(numList):
    middle = len(numList)//2
    return numList[middle]

def mode(numList):
    checked = []
    count = 0
    mode = numList[0]
    for x in numList:
        if x in checked:
            continue
        currentCount = 0
        for y in numList:
            if x == y:
                currentCount += 1
        if currentCount > count:
            mode = x
        checked.insert(x,0)
        count = currentCount
    return mode

def frequency(numList):
    checked = []
    result = {}
    for x in numList:
        if x in checked:
            continue
        Count = 0
        for y in numList:
            if x == y:
                Count += 1
        checked.insert(0,x)
        result[x] = Count
        
    
    return result

def Range(numList):
    Range = numList[-1] - numList[0]
    
    return Range

lst = [2,5,5,6,8,9,99,100]

"""
print(mean(lst))
print(median(lst))
print(mode(lst))
print(frequency(lst))
print(Range(lst))"""