"""
Author:Callum Egan
05/05/26
SUMMER OF'69: Return the sum of the numbers in the array, except ignore sections of
numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least
one 9). Return 0 for no numbers.
"""
def summer_69(lst):
    in_69 = False
    total = 0
    for x in lst:
        if x == 6:
            in_69 = True
        elif in_69 == True:
            if x == 9:
                in_69 = False
            continue
        else:
            total += x
    return total

lst = eval(input("enter a list of numbers: "))
print(summer_69(lst))