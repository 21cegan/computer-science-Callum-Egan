"""
Author:Callum Egan
10/9/25
Description: Set a variable called total to 0. Ask the user to enter five numbers. After each 
input ask if they wish to add that number to the total. If they do, add the number 
else do not add the number. When they have entered five numbers, display the 
total. 
"""
total = 0
for x in range(5):
    number = int(input("enter a number: "))
    if input("do you want to add this to the total?: ") == "yes":
        total += number
print(total)