"""
Author:Callum Egan
1/9/25
Description:Ask the user to enter their favourite colour. If they enter ‘red’, ‘RED’, or ‘Red’ –
display the message ‘I like red too’. Otherwise, display the message ‘ I don’t like 
the colour <user_colour>, I prefer red’
"""
colour = input("What is your favorite colour?: ")
if colour.lower() == "red":
    print("i like red too")
else:
    print(f"i dont like {colour} i prefer red")
    