"""
Author:Callum Egan
17/11/25
Description: Binary adder
"""
num1 = input("Enter a binary number: ")
num2 = input("Enter another binary number: ")
carry = 0
total = ""
if len(num1) >= len(num2):
    length = len(num1)
else:
    length = len(num2)
    
for x in range(1,length+1):
    digit = 0
    if len(num1) >= x:
        digit += int(num1[-x])
    if len(num2) >= x:
        digit += int(num2[-x])
    digit += carry
    if digit >= 2:
        carry = 1
        digit -= 2
    else:
        carry = 0
        
    total = str(digit) + total
    if x == length and carry == 1:
        total = str(carry) + total
print(total)
        