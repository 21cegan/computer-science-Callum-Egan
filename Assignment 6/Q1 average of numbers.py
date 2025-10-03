"""
Author:Callum Egan
2/10/25
Description:  Q1. Write a program that takes integers from the user and returns the average. Use a 
while loop and make an empty string the stop criteria
"""
total = 0
amount = 0
while True:
    userInput = input("enter an integer or hit enter to leave: ")
    if userInput == "":
        break
    else:
        total = total + int(userInput)
        amount += 1
average = total / amount
print(average)
