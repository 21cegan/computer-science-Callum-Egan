"""
Author:Callum Egan
1/9/25
Description:input 2 numbers and sort them in size
"""
number1 = int(input("input a number: "))
number2 = int(input("input another number: "))

if number1 > number2:
    print(number2, number1)
elif number2 > number1:
    print(number1, number2)
    
