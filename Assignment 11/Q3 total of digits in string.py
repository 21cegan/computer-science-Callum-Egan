"""
Author:Callum Egan
24/10/25
Description: Q3. Write a program to take in a string which is a mixture of characters. Extract all the
digits from the string and print their total.
Example input/output:
Input: Ab2 n4lksdf$89lkjd9%lskj f34
Output: The sum of the digits in the string is: 39
"""
string = input("Enter a string: ")
total = 0
for x in string:
    if x.isdigit():
        total += int(x)
print(total)