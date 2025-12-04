"""
Author:Callum Egan
25/11/25
Description: UTF encoder and decoder
"""
#encoding
hexa = ["A","B","C","D","E","F"]
decimal = [10,11,12,13,14,15]
if input("Enter 'e' to encode or anything else to decode: ") == "e":
    
    UTF = input("Enter a UTF value: U+")
    binary = ""
    for x in UTF:
        if x in hexa:
            x = decimal[hexa.index(x)] #turns decimal numbers above 10 into hexadecimal
        digit = ""
        remainder = 0
        x = int(x)
        while x > 0:
            
            remainder = x % 2
            digit = str(remainder) + digit
            x //= 2
            
        while len(digit) < 4:
            digit = "0" + digit #add 0s to the digit to reach 4 binary digits per hexadecimal digits
        binary += digit
        
    binary = binary[binary.find("1"):] #cut the excess 0s off the start of the binary number
    
    if len(binary) <= 7: #check if binary can fit into the first row
        encoded = "0" + binary
        while len(encoded) !=8:
            encoded = "0" + encoded
            
    elif len(binary) <= 11: 
        encoded = binary[:-6] + " 10" + binary[-6:] #fits the binary digits into the row
        while len(encoded) !=14:
            encoded = "0" + encoded #adds extra 0s to fill in missing space
        encoded = "110" + encoded
        
    elif len(binary) <= 16:
        encoded = binary[:-12] + " 10" + binary[-12:-6] + " 10" + binary[-6:]
        while len(encoded) !=22:
            encoded = "0" + encoded
        encoded = "1110" + encoded
        
    elif len(binary) <= 19:
        encoded = binary[:-18] + " 10" + binary[-18:-12] + " 10" + binary[-12:-6] + " 10" + binary[-6:]
        while len(encoded) !=30:
            encoded = "0" + encoded
        encoded = "11110" + encoded
    
    print(encoded)

#decoding
else:
    
    encoded = input("Enter an encoded UTF value: ")
    binary = ""
    
    if encoded[0] != "0":
        while " " in encoded: #remove the row indicators
            first0 = encoded.index("0")
            space = encoded.index(" ")
            binary += encoded[first0+1:space]
            encoded = encoded[space+1:]
        encoded = encoded[2:]
    binary += encoded
    UTF = ""
    while binary:
        power = 0
        y = 0
        for x in binary[:-5:-1]: #gets the last 4 binary digits to convert to hexa
            y += int(x)*(2**power)
            power += 1
        binary = binary[:-4]
        if y in decimal:
            UTF = hexa[decimal.index(y)] + UTF #
        else:
            UTF = str(y) + UTF
    print("U+"+UTF)
