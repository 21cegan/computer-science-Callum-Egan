"""
Callum Egan
12/8/2025
accumulator excersises
"""
#Q1
total = 0
for x in range(51):
    total += x
print(total)

#Q2
total2 = 0
n = int("!2: Enter an interger: ")
for x in range(n+1):
    total2 += x
print(total2)

#Q3
total3 = 1
for x in range(6):
    total3 *= x
print(total3)

#Q4
total4 = 0
for x in range(51):
    if x % 2 == 0:
        total4 += x
print(total4)

#Q5
total5 = 0
n = input("Q5: Enter a number: ")
for x in range(51):
    if x % 2 != 0:
        total5 += x
print(total5)

#Q6
total6 = 0
for x in range(51):
    if x % 3 == 0:
        total6 += x
print(total6)

#Q7
total7 = 1
for x in range(1,51):
    if x % 2 == 0:
        total7 *= x
print(total7)

#Q8
total8 = 1
for x in range(1,51):
    if x % 5 == 0:
        total8 *= x
print(total8)

#Q9
total = 0
for x in range(11):
    total += x*2
print(total)