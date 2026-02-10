"""
Author:Callum Egan
10/02/25
Description: Random Excersises 2
"""
import random

print("Welcome to my dice game!")
name = input("Please enter your name: ")
lucky_number = int(input("Enter a lucky number from 1 - 6: "))
computer_die_roll = random.randint(1,6) #Initialise computer number
print(name+"'s lucky number was:",lucky_number)
print("The computer rolled:",computer_die_roll)

if lucky_number == computer_die_roll:
    print("You guessed correctly")

elif lucky_number > computer_die_roll:
    print("You guessed too high")
elif lucky_number < computer_die_roll:
    print("You guessed too low")