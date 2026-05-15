"""
Author:Callum Egan
15/05/26
Description: caeser cipher 2
"""

def caeserEncrypt(string,key):
    string = string.upper()
    newstring = ""
    for x in string:
        if not x.isalpha():
            newstring += x
            continue 
        y = ord(x) + 12
        if y > 90:
            y -= 26
        newstring += chr(y)
    return newstring
def caeserDecrypt(string,key):
    string = string.upper()
    newstring = ""
    for x in string:
        if not x.isalpha():
            newstring += x
            continue 
        y = ord(x) - 12
        if y < 65:
            y += 26
        newstring += chr(y)
    return newstring

if input("Do you want to (E)ncrypt or (D)ecrypt: ").upper() == "E":
    print(caeserEncrypt(input("Enter a string to encrypt: "),int(input("Enter a key: "))))
else:
    print(caeserDecrypt(input("Enter a string to decrypt: "),int(input("Enter a key: "))))

