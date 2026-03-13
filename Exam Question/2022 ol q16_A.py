"""
Author:Callum Egan
23/10/25
Description: Question 16 A
"""
lenght = 6
width = 4

print("This program can find the perimeter or area of a quadrilateral")
length = float(input("Please enter the length: "))
width = float(input("Please enter the width: "))

name = input("Please enter your name: ")
choice = input("Do you want to find (p)erimeter or (a)rea?")

if choice == "p":
    print("A quadrilateral with a lenght of",length,"and an width of",width,"has a perimeter of:",round(length*2 + width*2,2))
elif choice == "a":
    print(round("A quadrilateral with a lenght of",length,"and an width of",width,"has an area of",length*width,2))
print("Thank you for using the program", name)