"""
Author:Callum Egan
15/12/25
Description: November Assessment Programming revision 1
"""
string = input("Enter a card number: ")

#Step 1
newString = string[:-1]
lastChar = string[-1]

#Step 2
newString = newString[::-1]

#Step 3
oddIndex = newString[1::2]
oddTotal = 0
for x in oddIndex:
    oddTotal += int(x)
    
evenIndex = newstring[::2]
evenTotal = 0
for x in evenIndex:
    x = int(x)
    x *= 2
    if x > 9:
        x -= 9
    evenTotal += 9
#Step 4   
total = evenTotal + oddTotal + int(lastChar)
#Step 5
if total % 10 == 0:
    print("Valid")
else:
    print("Invalid")