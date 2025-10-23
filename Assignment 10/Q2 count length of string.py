"""
Author:Callum Egan
23/10/25
Description: Exercise 2
Write a program to calculate the length of a string using :
i) A for loop
ii) A while loop
"""
string = input("Enter a string: ")
count = 0
for x in string:
    count += 1
print(count)

count = 0
while True:
    count +=1
    try:
        letter = string[count]
    except:
        break
print(count)