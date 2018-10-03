#This is a tip calculator
print("""Hello!
Welcome to Gabe\'s tip Calculator""")

cost_of_food = float(input("Enter Cost of Food: "))
sales_tax = cost_of_food * 0.0825
food_w_tax = cost_of_food + sales_tax
tip_input = float(input("Tip Percentage: "))
tip_conversion = tip_input / 100
tip = cost_of_food * tip_conversion
tip_new = round(tip, 2)
sales_tax = cost_of_food * 0.0825
total = food_w_tax + tip
print("Your Tip comes out to $", tip_new)
new_total = round(total, 2)
new_sales_tax = round(sales_tax, 2)
print("Sales Tax:",new_sales_tax)
print("Your total is $", new_total)


#Income tax Calculator
