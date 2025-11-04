"""
Author:Callum Egan
03/11/25
Description: Q13 count vowels in text
"""
string = input("Enter a string of characters: ")
vowels = ["a","e","i","o","u"]
count = 0
for x in string:
    if x in vowels:
        count +=1
print("There are",count,"vowels in this string")