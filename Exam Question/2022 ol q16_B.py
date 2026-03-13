"""
Author:Callum Egan
23/10/25
Description: Question 16 B
"""
import random

computer_options = ["rock","paper","scissors"]
computer_choice = computer_options[random.randint(0,2)]

user_choice = input("Enter rock, paper or scissors: ")
print("Player chose:",user_choice)
print("Computer chose:",computer_choice)

if user_choice == computer_choice:
    print("Draw!")
elif user_choice == "rock" and computer_choice == "paper" or user_choice == "paper" and computer_choice == "scissors" or user_choice == "scissors" and computer_choice == "rock":
    print("Computer wins!")
elif if user_choice == "scissor" and computer_choice == "paper" or user_choice == "rock" and computer_choice == "scissors" or user_choice == "paper" and computer_choice == "rock":
    print("Player wins!")
    