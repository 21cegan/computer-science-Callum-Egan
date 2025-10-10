"""
Author:Callum Egan
8/10/25
Description:  13. Take integer a as an input and check whether it ends in 4 or 8.
"""

number = input("Enter an integer")
lastdigit = number[-1]

if lastdigit == "4":
    print("Ends with 4")
elif lastdigit == "8":
    print("Ends with 8")
else:
    print("Ends with neither")
