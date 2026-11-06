"""
Author:Callum Egan
5/11/26
Description:number of characters in string
"""

def stringLength(s):
    if not s:
        return 0
    else:
        return 1 + stringLength(s[1:])

string = input("Enter a string: ")
print(stringLength(string))
