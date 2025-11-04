"""
Author:Callum Egan
03/11/25
Description: Q10 Turn numbers into roman numerals
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000. 
"""
number = input("Enter a number: ")

thousands = int(number[-4])
hundreds = int(number[-3])
tens = int(number[-2])
ones = int(number[-1])
roman = ""

roman += "M"*thousands
if hundreds == 9:
    roman += "CM"
elif hundreds == 4:
    roman += "CD"
elif 9 > hundreds >= 5:
    roman += "D" + "C"*(hundreds -5)
else:
    roman += "C"*(hundreds)
    
if tens == 9:
    roman += "XC"    
elif tens == 4:
    roman += "XL"
elif 9 > tens >= 5:
    roman += "L" + "X"*(tens -5)
else:
    roman += "X"*(tens)

if ones == 9:
    roman += "IX"
elif ones == 4:
    roman += "IV"
elif 9 > ones >= 5:
    roman += "V" + "I"*(ones -5)
else:
    roman += "I"*ones

print(roman)
