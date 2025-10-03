"""
Author:Callum Egan
3/10/25
Description:  Q8. Write a program which asks the user to guess a value you have set in your code. The 
program should tell them if their guess is too high or too low and print a well done 
message when they guess it correct telling them how many attempts it took.
"""
number = 23
number = float(number)
while True:
    Guess = input("Enter a number: ")
    Guess = float(Guess)
    if Guess == number: 
        print("Well done")
        break
    elif Guess < number:
        print("too low")
    elif Guess > number:
        print("too high")