"""
Author:Callum Egan
3/10/25
Description:  Q5. Write a program that prints from 1 to n squared using a while loop. It should stop the 
while loop if the iteration count is 50. (Hint use break)
"""
number = input("Enter a number: ")
number = int(number)
n = 1
while n <= number**2:
    print(n)
    if n == 50:
        break
    n += 1