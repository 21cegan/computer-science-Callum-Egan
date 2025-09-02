"""
Author:Callum Egan
1/9/25
Description:compute simple and compound interest
"""
interestType = input("simple or compound interest?: ")
startMoney = float(input("how much money did you start off with?: "))
rate = float(input("What is the percentage interest rate per period?: "))
rate = rate/100
time = int(input("how many periods are you getting interest?: "))

if interestType == "simple":
    finalAmount = startMoney + startMoney * rate * time
    
elif interestType == "compound":
    finalAmount = startMoney*(1 + rate)**time
    
print(f"At the end, you will have €{round(finalAmount, 2)}")