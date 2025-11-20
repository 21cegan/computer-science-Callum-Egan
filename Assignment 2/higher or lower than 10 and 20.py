"""
Author:Callum Egan
1/9/25
Description: Ask the user to enter a number. If it is under 10, display the message ‘Too low’, if 
their number is between 10 and 20 display ‘Correct’, otherwise display ‘Too high’
"""
number = int(input("enter a number: "))

if number > 20:
    print("too high")
elif number < 10:
    print("too low")
else:
    print("correct")
