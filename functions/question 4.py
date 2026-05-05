"""
Author:Callum Egan
30/04/26
Description: OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a
name. If the name is too short it should return an error number
"""
def old_macdonald(string):
    return string[0].upper()+string[1:3]+string[3].upper()+string[4:]
print(old_macdonald("macdonald"))