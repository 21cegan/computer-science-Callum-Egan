"""
Author:Callum Egan
1/9/25
Description:sk the user to enter three number. Add together the first two and store this
answer in a variable. Then multiply this result by the third. Display the answer as: 
The answer is: <calculated result>
"""
numberA = int(input("type a number: "))
numberB = int(input("type a second number: "))
numberC = int(input("type a third number: "))

numberAB = numberA + numberB

print("the answer is: ", numberAB*numberC)
