"""
Author:Callum Egan
1/9/25
Description:Ask the user for their name and their age. Calculate their age next year and then 
display the message: Hello <user_name>, next year you will be <new_age> years 
old.
"""
name= input("what is your name?: ")
age = int(input("how old are you?: "))
print(f"Hello {name}, next year you will be {age+1} years old")