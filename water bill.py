"""
Author:Callum Egan
1/9/25
Description:  Write a program to display the total water bill charges for a month given the 
number of units consumed. Your calculation should be based on the following 
rates: 
• 5 cent a unit for the first 100 units
• 10 cent a unit for the next 150 units
• 20 cent a unit for any over 250
"""
water = int(input("How much units of water did you use: "))
bill = 0
if water >= 100:
    bill += 100*5
    water -= 100
    if water >= 150:
        bill += 150*10
        water -= 150
        bill += water*20
    else:
        bill += water*10
else:
    bill += water*5
bill = bill/100
print(f"your bill is €{bill}")