"""
Author:Callum Egan
10/10/25
Description:  Q18. read integer x, have the number of digits in x as the 10s place in Y,
and the most significant digit as the 1s place
"""

x = input("Enter and integer: ")
list = []
for digit in x:
    digit = int(digit)
    list.append(digit)
y = len(x)*10 + list[0]
print(y)