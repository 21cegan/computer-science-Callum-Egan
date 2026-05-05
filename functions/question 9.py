"""
Author:Callum Egan
05/05/26
BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to
21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum
by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
"""
def blackjack(a,b,c):
    total = a + b + c
    if total <= 21:
        return total
    else:
        if 11 == a or 11 == b or 11 == c:
            return total-10
        else:
            return "BUST"
print(blackjack(9,9,11))