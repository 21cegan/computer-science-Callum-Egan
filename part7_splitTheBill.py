"""
Author:Callum Egan
1/9/25
Description:Ask the user for the total price of the bill. Then, ask for the number of diners and 
output a message saying how much each person must pay
"""

bill = int(input("how much is the total bill?: "))
NumOfPeople = int(input("how many people are there?: "))

print("each person pays", bill/NumOfPeople)