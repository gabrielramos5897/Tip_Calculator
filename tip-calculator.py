#This is a tip calculator
print("Tip Calculator")

cost_of_food = float(input("Enter Cost of Food: "))
if cost_of_food >= 200:
    print("Wow..Big Spender")
elif cost_of_food <= 10:
    print("Don't leave a tip dude")
else:
    exit()

sales_tax = cost_of_food * 0.0825
food_w_tax = cost_of_food + sales_tax

tip_input = float(input("Tip Percentage: "))
if tip_input <= 5:
    print("Dude leave a biggere tip")
    tip_input = float(input("Tip Percentage: "))


tip_conversion = tip_input / 100
tip = cost_of_food * tip_conversion
tip_new = round(tip, 2)
sales_tax = cost_of_food * 0.0825
total = food_w_tax + tip
new_total = round(total, 2)
new_sales_tax = round(sales_tax, 2)

print("Your Tip comes out to $", tip_new)
print("Sales Tax:",new_sales_tax)
print("Your total is $", new_total)

#Income tax Calculator
