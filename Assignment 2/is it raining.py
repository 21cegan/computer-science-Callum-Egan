"""
Author:Callum Egan
1/9/25
Description: Ask the user if it is raining. If they enter ‘yes’ or ‘Yes’ ask if it is windy. If they 
answer ‘yes’ or ‘Yes’ to the second question display the message ‘ It is too windy 
for an umbrella’, otherwise, display the message ‘Take an umbrella’. If they did 
not answer yes to the first question, display the answer ‘Enjoy your day’.
"""

if input("is it raining?: ").lower() == "yes":
    if input("is it windy?: ").lower() == "yes":
        print ("is it too windy for an umbrella? ")
    else:
        print("take an umbrella")
else:
    print("Enjoy your day")
