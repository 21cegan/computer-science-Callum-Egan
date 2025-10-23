"""
Author:Callum Egan
21/10/25
Description:  Exercise 3
For this question you may need to use indexing, slicing and the replace() method.
Create a string from a given string where all occurrences of its first char have been 
changed to '$', except the first char itself.
Example input/output:
User inputs ‘restaurant’
The first letter is ‘r’
The new string will have all occurrences of the letter ‘r’, replaced with ‘$’ except for the 
first occurrence
Output should be: restau$ant
Example input/output:
User inputs ‘anaconda’
Output: an$cond
"""
string = input("Enter a string: ")
string = string[0] + string[1:].replace(string[0],"$")
print(string)
