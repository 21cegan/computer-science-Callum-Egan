"""
Author:Callum Egan
14/05/26
Description: caeser cipher 1
"""

alphabet =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
def caeserEncrypt(string,key):
    string = string.upper()
    newstring = ""
    for x in string:
        if x in alphabet:
            letter = alphabet.index(x) + key
            if letter >= 26:
                letter %= 26
            newstring += alphabet[letter]
        else:
            newstring += x
    return newstring

def caeserDecrypt(string,key):
    string = string.upper()
    newstring = ""
    for x in string:
        if x in alphabet:
            letter = alphabet.index(x) - key
            if letter < 0:
                letter %= 26
            newstring += alphabet[letter]
        else:
            newstring += x
    return newstring

if input("Do you want to (E)ncrypt or (D)ecrypt: ").upper() == "E":
    print(caeserEncrypt(input("Enter a string to encrypt: "),int(input("Enter a key: "))))
else:
    print(caeserDecrypt(input("Enter a string to decrypt: "),int(input("Enter a key: "))))