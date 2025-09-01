"""
Author:Callum Egan
1/9/25
Description:Ask the user how many slices of pizza they started with. Then ask them how 
many they have eaten. Work out how many are left and display this result to the 
user. 
"""

WholePizza= int(input("how many slices of pizza were there?: "))
eatenSlices = int(input("how many slices did you eat?: "))

print("you have", WholePizza-eatenSlices, "slices left.")