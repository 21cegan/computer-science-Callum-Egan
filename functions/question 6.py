"""
Author:Callum Egan
30/04/26
Description: ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
"""
def almost_there(num):
    if num >= 90 and num <= 110 or num >= 190 and num <= 210:
        return True
    else:
        return False
print(almost_there(89))