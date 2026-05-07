"""
Author:Callum Egan
05/05/26
excersise 2
"""

def lstrange(lst):
    lst.sort()
    listRange = lst[-1]-lst[0]
    return listRange

def lst_average(lst):
    total = 0
    total=total
    for x in lst:
        total += x
    return total / len(lst)

def lst_median(lst):
    lst.sort()
    n = len(lst)
    if n % 2 == 0:
        median = n/2
    else:
        median = (n+1)/2
    return lst[int(median)-1]

def lst_mode(lst):
    mode = 0
    mode_count =0
    for x in lst:
        x_count = 0
        for y in lst:
            if x == y:
                x_count += 1
        if x_count > mode_count:
            mode = x
            mode_count = x_count
    return mode
            
def lst_frequency(lst):
    counted = []
    counts = []
    
    for x in lst:
        if x in counted:
            continue
        else:
            counted.append(x)
            counts.append(lst.count(x))
    return counted, counts     
    
startlst = eval(input("Enter a list of numbers: "))
print("range: ",lstrange(startlst))
print("average: ",lst_average(startlst))
print("median: ",lst_median(startlst))
print("mode: ",lst_mode(startlst))

counted,counts = lst_frequency(startlst)
for i in range(len(counted)):
    print(counted[i],"appears",counts[i], "times")