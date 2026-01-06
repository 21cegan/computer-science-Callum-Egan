"""
Author:Callum Egan
06/01/26
Description: November Assessment Programming revision Question 1 Version 2
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

    firstDigit = int(cardNum[-16])
    if firstDigit == 7:#boolean
        print("This is a ZincCard")
    elif firstDigit == 8:#boolean
        print("This is a Wincard")
    expire = input("Enter the card's expiry date: ")
    cvv = 0
    for x in range(0,4):
        cvv += int(expire[x])
    cvv *= int(cardNum[-16:-14])
    cvv -= int(cardNum[9])
    print("CVV number:",cvv)
    print("Card number:", cardNum[:4]+"-"+cardNum[4:8]+"-"+cardNum[8:12]+"-"+cardNum[12:],"and it is valid.")
    
    
else:#boolean
    print("Too many incorrect attempts")

