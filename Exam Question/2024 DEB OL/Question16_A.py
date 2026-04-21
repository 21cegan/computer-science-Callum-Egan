# Question 16(a)
# Name and School:Callum Egan

print("Household budget calculator. Enter the following information:")
num_adults = int(input("Number of Adults in household: "))
num_child = int(input("Number of Children in household: "))

inflation_rate = float(input("Inflation rate (e.g. 0.05 for 5% inflation): "))

food_budget = 300
cost_food_adults = 50
cost_food_child = 35

child_allowance = 140
child_allowance_total = child_allowance*num_child
if num_child > 3:
    child_allowance_total += 20*(num_child-3)

food_cost_total = cost_food_adults*num_adults+cost_food_child*num_child
food_cost_inflation = food_cost_total*(1+inflation_rate)

print("Children’s allowance total: €", child_allowance_total)
print("Total household food cost: €",food_cost_total)
print("Total household food cost with inflation: €",round(food_cost_inflation,2))
print("Percentage spent on food:", round(food_cost_inflation/child_allowance_total*100,2),"%")
print("Budget remaining after food spent: €",food_cost_inflation+child_allowance_total-food_cost_total)
