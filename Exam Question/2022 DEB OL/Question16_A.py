# Question 16(a) 
# Name and School:Callum Egan 
import random
 
while True:
    s_name = input("Enter your surname: ")
    f_name = input("Enter your first name: ")
    age = int(input("Enter your age: "))
    eircode = input("Enter your Eircode: ")
    
    vaccine = ""
    if input("Do you agree to enroll in a vaccine trial? \n Type 'Yes' or 'No': ").upper() == "YES":
        vaccine = random.choice(["A","B","C"])

    print("Hello", f_name, s_name, "you are", age, "years old and your aircode is", eircode)

    if int(eircode[-1]) % 2 == 0:
        print("You must attend Eastwood for your vaccine")
    else:
        print("You must attend Northfield for your vaccine")
       
    if vaccine:
        print("You are now enrolled in the trial to recieve Super vaccine", vaccine)
    elif age >= 50:
        print(f_name+ ", you will recieve the ADENO vaccine")
    else:
        print(f_name+ ", you will recieve the MRNA vaccine")

    if input("If you have finished entering people's details type 'END' otherwise press RETURN: ").upper() == "END":
        break

