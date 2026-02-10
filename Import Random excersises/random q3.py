"""
Author:Callum Egan
09/02/25
Description: Random Excersises q3
"""
import random
if random.randint(1,2) == 1:
    side = "heads"
else: side = "tails"

if input("Heads or tails: ") == side:
    print("Correct")
else:
    print("Incorrect")
print(side)