"""
Author:Callum Egan
17/10/25
Description:  Q3. Ask the user to enter a word and print the word modified as follows:
• If the first letter of the word is a vowel, add ‘way’ to the end. So, if the user enters 
‘apple’ it should output ‘appleway’. 
• If the first letter of the word is a consonant, move the first letter to the end and 
add ‘ay’. So, if the user enters ‘pear’, it should output ‘earpay’.
"""
word = input("Enter a word: ")
vowel = ["a","e","i","o","u"]
if word[0].lower() in vowel:
    print(word+"way")
else:
    newWord = word[1:] + word[0] + "ay"
    
    print(newWord)