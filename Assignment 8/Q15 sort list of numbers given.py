"""
Author:Callum Egan
9/10/25
Description:  Q15. Find the largest number of a list of numbers entered
"""
list = []
try:
    while True:
        number = input("Enter a number or anything else to stop: ")
        number = int(number)
        if list:
            if number > list[0]:
                list.insert(0,number)
            else:
                list.append(number)
        else:
            list.append(number)
except:
    print(list[0])