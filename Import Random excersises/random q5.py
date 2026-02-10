"""
Author:Callum Egan
09/02/25
Description: Random Excersises q5
"""
import random

signs = ["+","-","//","*"]

points = 0
while True:
    num1 = random.randint(0,100)
    num2 = random.randint(0,100)
    sign = random.choice(signs)

    if sign == "+":
        answer = num1 + num2
    elif sign == "-":
        answer = num1 - num2
    elif sign == "//":
        answer = num1 // num2
    elif sign == "*":
        answer = num1 * num2

    userInput = input(f"What is {num1} {sign} {num2} (or enter q to leave): ")
    if userInput == str(answer):
        points += 1
        print("Correct! You now have",points,"points")
        continue
    elif userInput == "q":
        break
    else:
        print("Incorrect, the anwer was",answer)
    
