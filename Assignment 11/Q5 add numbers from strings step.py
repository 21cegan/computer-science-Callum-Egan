"""
Author:Callum Egan
24/10/25
Description: Q5. Write a program which asks the user to enter a string of digits, and a step size.
Go through the string and add the first number plus all the numbers at the step size.
Example input/output:
Enter a string of digits: 123456789
Enter a step size: 3
#The total is the first number, plus every third number after since the step size is 3
Output: Total is equal to: 1 + 4 +7 = 12
Example input/output:
Enter a string of digits: 123456789102321
Enter a step size: 4
#The total is the first number, plus every fourth number after since the step size is 4
Output: Total is equal to: 1 + 5 +9 + 3 = 18
"""
digits = input("Enter a a string of digits: ")
step = int(input("Enter a step size: "))

newstring = digits[::step]
total = 0
for x in newstring:
    total += int(x)
print(total)