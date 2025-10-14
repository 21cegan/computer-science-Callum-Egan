"""
Author:Callum Egan
10/10/25
Description:  Q20. Continue sequences
"""

denominator = 9
numerator = 2
sign = 1
total = 0
for x in range(0,7):
    total += sign * numerator / denominator
    denominator += 4
    numerator += 3
    sign *= -1
print(total)

n = int(input("Enter an integer: "))
total = 0
for x in range(1,n+1):
    if x % 2 == 0:
        continue
    total += int(x)**2
print(total)