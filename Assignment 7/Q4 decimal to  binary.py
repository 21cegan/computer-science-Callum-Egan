"""
Author:Callum Egan
7/10/25
Description:  4. Write a program to convert Decimal to Binary
"""
decimal = input("Enter a decimal number: ")
binary = []
decimal = int(decimal)
while decimal != 0:
    remainder = decimal % 2
    
    binary.insert(0,int(remainder)) #adds the result to the first place in the list
    
    if remainder == 1:
        decimal -= 1
    decimal /= 2
binarystr = ""
for x in binary:
    binarystr += str(x) #turns the list into a string so that it looks nicer
print(binarystr)


