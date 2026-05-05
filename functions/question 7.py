"""
Author:Callum Egan
30/04/26
Description: Given a list of ints, return True if the array contains a 3 next to a 3 somewhere."""
def has_33(lst):
    prev = False
    for x in lst:
        if x == 3:
            if prev == True:
                return True
            else:
                prev = True
        else:
            prev = False
    return False
print(has_33([3,1,3]))