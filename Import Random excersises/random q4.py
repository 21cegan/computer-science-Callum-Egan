"""
Author:Callum Egan
09/02/25
Description: Random Excersises q4
"""
import random
number = random.randint(1,100)

guess = input("Guess the number between 1 and 100")
attempts = 7
while guess != number and attempts != 0:
    print("Incorrect,",attempts,"tries left")
    guess = input("Guess the number between 1 and 100")
    
if attempts == 0:
    print("you lose, the number was", number )
else:
    print("You win")