"""
Author:Callum Egan
15/12/25
Description: November Assessment Programming revision 3
"""
string = input("Enter a card number: ")
#Step 1
newString = string[:-1]
lastChar = string[-1]
#Step 2
revString = ""
charNum = 0
for x in range(0,len(newString)):
    revString = newString[charNum] + revString
    charNum += 1
#Step 3
oddTotal = 0
evenTotal = 0
for x in range(0,len(revString)):
    x = int(x)
    if x % 2 == 0:
        x *= 2
        if x > 9:
            x -=9
        evenTotal += x
    else:
        oddTotal += x
#Step 4  
total = evenTotal + oddTotal + int(lastChar)
#Step 5
if total % 10 == 0:
    print("Valid")
else:
    print("Invalid")

