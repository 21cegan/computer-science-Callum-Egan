"""
Author:Callum Egan
05/05/26
SPY GAME: Write a function that takes in a list of integers and returns True if it contains 
007 in order
"""

def spy_game(lst):
    has0 = False
    has00 = False
    
    for x in lst:
        if x== 0:
            if has0:
                has00 = True
            has0 = True
        elif has00 and x == 7:
            return True
    return False



lst = eval(input("enter a list of numbers: "))
print(spy_game(lst))