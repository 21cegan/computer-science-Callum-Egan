"""
Author:Callum Egan
7/10/25
Description:  2. Write a program to enter numbers until the user enters 0. Then it should print the 
count of the positive and negative numbers entered. You can assume all input is 
numeric.
"""
negatives = 0
positives = 0
while True:
    number = int(input("Enter a number or enter 0 to stop: "))
    if number > 0:
        positives += 1
    elif number < 0:
        negatives += 1
    elif number == 0:
        break
print(f"You typed {positives} positive numbers and {negatives} negative numbers")