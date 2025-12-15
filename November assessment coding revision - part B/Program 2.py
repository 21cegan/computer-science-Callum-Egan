"""
Author:Callum Egan
15/12/25
Description: November Assessment Programming revision 2
"""
string = input("Enter a card number: ")
#Step 1
newString = string[:-1]
lastChar = string[-1]

#Step 2
revString = ""
for char in newString:
    revString = char + revString
#Step 3
oddIndex = ""
for num in range(1,len(revString),2):
    oddIndex += revString[num]   
oddTotal = 0
for x in oddIndex:
    oddTotal += int(x)
    
evenIndex = ""
for num in range(0,len(revString),2):
    evenIndex += revString[num]
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
