#Question16_B_OL
#Enter your name here:Callum Egan
print("Welcome to my weekly step tracker!")

StepsList = []
StepsList.append(int(input("Please enter the steps you did on Monday:")))
StepsList.append(int(input("Please enter the steps you did on Tuesday:")))
StepsList.append(int(input("Please enter the steps you did on Wednesday:")))
StepsList.append(int(input("Please enter the steps you did on Thursday:")))
StepsList.append(int(input("Please enter the steps you did on Friday:")))
StepsList.append(int(input("Please enter the steps you did on Saturday:")))
StepsList.append(int(input("Please enter the steps you did on Sunday:")))

print("The list of steps is:", StepsList)

totalSteps = 0
for x in StepsList:
    totalSteps += x

print("The total steps taken this week was:", totalSteps)
print("The average number if steps is:", totalSteps/7)

StepsList.sort()
print("The largest number of steps you took this week was:", StepsList[-1])
print("The smallest of steps you took this week was:", StepsList[0])

