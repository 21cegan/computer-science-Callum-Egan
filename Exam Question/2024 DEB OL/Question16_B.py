# Question 16(a)
# Name and School:Callum Egan

principal = float(input("Enter the principal investment amount: €"))
interest = float(input("Enter the annual interest rate (e.g. 0.05 for 5% interest): "))
for t in range(1,11):
    print("Year",t,"Investment value: €", round(principal*((1+interest)**t),2))