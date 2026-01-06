"""
Author:Callum Egan
05/01/26
Description: November Assessment Programming revision Question 1 Version 1
"""
#cardNum = 7200828282828210
cardNum = input("Welcome to CardCheck. Enter your card number: ")
lengthCheck = False #boolean
attempts = 1
while attempts < 3 and not lengthCheck: #boolean
    attempts +=1
    if len(cardNum) == 16:#boolean
        lengthCheck = True#boolean
    else:#boolean
        cardNum = input("That is incorrect, please try again: ")
if lengthCheck:#boolean
    print(cardNum)

    firstDigit = int(cardNum)
    while firstDigit > 10:#boolean
        firstDigit //= 10
    if firstDigit == 7:#boolean
        print("This is a ZincCard")
    elif firstDigit == 8:#boolean
        print("This is a Wincard")
    expire = int(input("Enter the card's expiry date: "))
    cvv = 0
    while expire != 0:#boolean
        cvv += expire % 10
        expire //= 10
    cvv *= int(cardNum[0:2])
    cvv -= int(cardNum[9])
    print("CVV number:",cvv)
    print("Card number:", cardNum[:4]+"-"+cardNum[4:8]+"-"+cardNum[8:12]+"-"+cardNum[12:],"and it is valid.")
    
    
else:#boolean
    print("Too many incorrect attempts")
