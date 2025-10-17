"""
Author:Callum Egan
17/10/25
Description:  Q4. Write a program to count the number of times a character occurs in the given string.
The string and the character should be input by the user.
"""
word = input("Enter a string: ")
letter = input("Enter a character: " )
count = 0
if len(letter) > 1:
    print("only one letter")
else:
    for x in word:
        if x == letter:
            count += 1
    print(f"The letter {letter} appears {count} time(s) in the string '{word}'")