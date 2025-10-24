"""
Author:Callum Egan
24/10/25
Description: Q4. Write a program which asks the user to guess a number between 1 and 100
inclusive. You can hardcode the number they are trying to guess. Prompt the user if they
are too high or too low. They can have no more than 7 attempts. If they use more then 7
print ‘Game Over’ and tell them the answer.
"""
number = 58
for x in range(1,7):
    guess = int(input("Guess a number between 1 and 100: "))
    if guess == number:
        print("You win!")
        exit()
    elif guess > number:
        print("too high")
    elif guess < number:
        print("too low")
print("Game Over, the number was", number)