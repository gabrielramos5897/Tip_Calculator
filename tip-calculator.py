#This is a tip calculator
print("""Hello!
Welcome to Gabe\'s tip Calculator""")

cost_of_food = float(input("Enter Cost of Food: "))
tip_input = float(input("Amount to tip: "))
tip_conversion = tip_input / 100
tip = cost_of_food * tip_conversion
total = cost_of_food + tip
print("Your time comes out to ", tip)
new_total = round(total, 2)
print("Your total is $ ", new_total)


#Income tax Calculator
