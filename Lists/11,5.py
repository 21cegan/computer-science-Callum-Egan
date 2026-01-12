"""
Author:Callum Egan
08/01/26
Description: lists 11.5
"""
val = [17,23,18,19]
print("The list is : ",val)
while True:
    print("Main Menu")
    print("1. Insert")
    print("2. Delete")
    print("3. Exit")
    ch = int(input("Enter your choice (1/2/3): "))
    if ch == 1:
        item = int(input("Enter item: "))
        pos = int(input("At what position: "))
        index = pos - 1
        val.insert(index,item)
        print("Sucess! List is now:",val)
    elif ch == 2:
        print("Deletion Menu")
        print("1. Delete using Value")
        print("2. Delete using Index")
        print("3. Delete a Sublist")
        dch = int(input("Enter choice (1/2/3): "))
        if dch == 1:
            item = int(input("Enter item to be deleted: "))
            val.remove(item)
            print("List is now:",val)
        elif dch == 2:
            index = int(input("Enter index of item to be deleted: "))
            val.pop(index)
            print("list is now :",val)
        elif dch == 3:
            l = int(input("Enter lower limit of the slice to be deleted: "))
            h = int(input("Enter upper limit of list slice to be deleted: "))
            del val[l:h]
            print("List is now:", val)
        else: print("valid choices are 1/2/3 only.")
    elif ch == 3:
        break
    else:
        print("valid choices are 1/2/3 only.")