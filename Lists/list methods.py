"""
Author:Callum Egan
08/01/26
Description: list methods
"""
lst1 =[11,17,14,18,13,20]
val = [17,24,15,30]
"""
lst1.append(16)
print(lst1)

lst1.extend([8,5,19])
print(lst1)

myl =[2,4,6]
print("Current list is: ")
n = eval(input("Enter a number or list to append: "))
if type(n) == type([]):
    myl.extend(n)
elif type(n) == type(2):
    myl.append(n)
else:
    print("Please enter an integer or list")
print("Appended list is:",myl)

val.insert(2,115)
print(val)

lst1[2] = 56
print(lst1)

print(val.pop(2))
print(val)

val.remove(17)
print(val)

del lst1[2]
print(lst1)

del lst1[2:4]
print(lst1)
"""
#sortin lists

print(lst1.sort())
print(lst1.sort(reverse = True))
