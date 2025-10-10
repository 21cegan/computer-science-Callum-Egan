"""
Author:Callum Egan
8/10/25
Description:  14. Take N (N > 20) as an input. print numbers 11 to N, when number is multiple of 3, print "Tipsy",
when multiple of 7, print "Topsy", when multiple of both print "TipsyTopsy"
"""
N = input("Enter a number above 20: ")
try:
    N = int(N)
    if N > 20:
        for x in range(11,N):
            if x % 3 == 0 and x % 7 == 0:
                print("TipsyTopsy")
            elif x % 3 == 0:
                print("Tipsy")
            elif x % 7 == 0:
                print("Topsy")
            else:
                print(x)
except ValueError:
    print("Enter an integer")
