"""
Author:Callum Egan
1/9/25
Description:Ask the user to enter a random number of days. Output how many hours, 
minutes and seconds are in the given number of days.
"""
days = int(input("enter a number of days"))

hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print(f"In {days} days there are; \n {hours} hours \n {minutes} minutes \n {seconds} seconds")
