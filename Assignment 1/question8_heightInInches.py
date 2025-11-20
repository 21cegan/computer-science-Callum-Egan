"""
Author:Callum Egan
1/9/25
Description:Program that accepts height in centimetres and converts it to feet and inches
"""
heightcm = int(input("What is your height in centimetres?: "))
inches = heightcm/2.54
feet = inches // 12
inches= inches % 12
print(f"You are {int(feet)} foot {int(inches)} inches tall")
