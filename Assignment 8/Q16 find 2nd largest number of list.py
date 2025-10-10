"""
Author:Callum Egan
10/10/25
Description:  Q16. Find the 2nd largest number of a list of numbers entered
"""
list = []
try:
    while True:
        number = input("Enter a number or anything else to stop: ")
        number = int(number)
        if len(list) > 1:
            if number > list[0]:
                list.insert(0,number)
            elif number > list[1]:
                list.insert(1,number)
                
        elif len(list) == 1:
            if number > list[0]:
                list.insert(0,number)
                
        list.append(number)
except:
    print(list[1])
