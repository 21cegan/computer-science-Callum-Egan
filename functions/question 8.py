"""
Author:Callum Egan
30/04/26
PAPER DOLL: Given a string, return a string where for every character in the original
there are three characters
"""
def paper_doll(string):
    newStr = ""
    for x in string:
        newStr += x*3
    return newStr
print(paper_doll("hello"))

    