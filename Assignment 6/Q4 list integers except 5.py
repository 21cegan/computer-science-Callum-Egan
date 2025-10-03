"""
Author:Callum Egan
3/10/25
Description:  Q4. Write a program that prints from 1 to n using a while loop, it should skip every 
multiple of 5. (Hint, use % and continue)
"""
number = input("enter a number: ")
number = int(number)
n=1
while n <= number:
    if (n%5) != 0:
        print(n)
    n+=1