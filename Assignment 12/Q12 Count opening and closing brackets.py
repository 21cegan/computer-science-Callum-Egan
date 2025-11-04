"""
Author:Callum Egan
03/11/25
Description: Q12 find if there is an equal number of opening and closing brackets
"""

string = input("Enter a string of opening and closing brackets: ")
opening = string.count("(")
closing = string.count(")")
if opening == closing:
    print("Equal number of opening and closing brackets")
elif opening > closing:
    print("There are more opening brackets than closing ones")
else:
    print("There are more closing brackets than opening ones")