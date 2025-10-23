"""
Author:Callum Egan
21/10/25
Description:  Write some code to test all the Python string methods given on the Python reference 
guide
"""
string = " Hello There "
print(string.lower())
print(string.upper())

x = input("Enter a character: ")
print(string.count(x))

y = input("Enter a character to replace the first with: ")
print(string.replace(x,y))


string2 = input("Enter another string: ")

if string2.islower():
    print("all lowercase")
    
if string2.isupper():
    print("all uppercase")
    
if string2.isalnum():
    print("all alphanumeric")
    
if string2.isalpha():
    print("all alphabetic")
    
if string2.isdigit():
    print("all digits")
    
substring = input("Enter a smaller string to search for: ")
print(string2.index(substring))
print(string.strip())
    