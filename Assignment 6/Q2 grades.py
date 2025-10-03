"""
Author:Callum Egan
2/10/25
Description:  Q2. Write a program that takes test grades from the user and returns their average and 
the letter grade of the average. Use a while loop and make negative number the stop 
criteria. A >=90 B 80-89 C 70-79 D 60-69 F 59 or less
"""
while True:
    grade = input("Enter the Grade or enter a negative number to leave: ")
    grade = int(grade)
    if grade >= 90:
        print("A")
    elif grade >= 80:
        print("B")
    elif grade >= 70:
        print("C")
    elif grade >= 60:
        print("D")
    elif grade >= 0:
        print("F")
    else:
        break