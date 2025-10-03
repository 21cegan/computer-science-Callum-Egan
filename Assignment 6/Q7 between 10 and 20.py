"""
Author:Callum Egan
3/10/25
Description:  Q7. Write a program which asks the user to enter a number between 10 and 20
inclusive. If they enter a number less than 10, print ‘too low’. If they enter a number 
greater than 20 print ‘too high’. The program should continue until they enter a value 
between 10 and 20 then display the message ‘Thank you’
"""

while True:
    number = input("Enter a number between 10 and 20: ")
    number = float(number)
    if number >=10 and number <= 20:
        print("Thank you")
        break
    elif number < 10:
        print("too low")
    elif number > 20:
        print("too high")
    