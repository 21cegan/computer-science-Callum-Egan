"""
Author:Callum Egan
01/05/26
Description: MASTER YODA: Given a sentence, return a sentence with the words reversed
"""
def master_yoda(string):
    strList = string.split()
    return " ".join(strList[::-1])
print(master_yoda("i am home"))