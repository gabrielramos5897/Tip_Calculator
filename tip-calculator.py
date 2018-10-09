# This is a tip calculator

print("Tip Calculator")
mylist = ["new_york", "los_angeles", "houston", "austin",
          "dallas", "fort_worth", "portland", "denver", "salt lake", "atlanta"]
city_input = int(input("""
     0 New York City
     1 Los Angeles
     2 Houston
     3 Austin
     4 Dallas
     5 Fort Worth
     6 Portland
     7 Denver
     8 Salt Lake
     9 Atlanta

      Pick your City: """))

cost_of_food = float(input("Enter Cost of Food: "))
if cost_of_food >= 200:
    print("Wow..Big Spender")
elif cost_of_food <= 10:
    print("No need to leave a tip dude")

if city_input == 0:
    mylist[0] = sales_tax = cost_of_food * 0.08875
elif city_input == 1:
    mylist[1] = sales_tax = cost_of_food * 0.0888
elif city_input == 2:
    mylist[2] = sales_tax = cost_of_food * 0.0825
elif city_input == 3:
    mylist[3] = sales_tax = cost_of_food * 0.0825
elif city_input == 4:
    mylist[4] = sales_tax = cost_of_food * 0.0825
elif city_input == 5:
    mylist[5] = sales_tax = cost_of_food * 0.0825
elif city_input == 6:
    mylist[6] = sales_tax = 0
elif city_input == 7:
    mylist[7] = sales_tax = cost_of_food * 0.0810
elif city_input == 8:
    mylist[8] = sales_tax = cost_of_food * 0.0825
elif city_input == 9:
    mylist[9] = sales_tax = cost_of_food * 0.0890
else:
    sales_tax = cost_of_food * 0.0725
    print("""You either did not pick a city or placed an unkown character.
You were assigned the default Tax Rate of 7.25%.""")

if cost_of_food <= 10:
    tip_input = 0
else:
    tip_input = int(float(input("Tip Percentage: ")))

food_w_tax = cost_of_food + sales_tax
tip_conversion = tip_input / 100
tip = cost_of_food * tip_conversion
tip_new = round(tip, 2)
total = food_w_tax + tip
new_total = round(total, 2)
new_sales_tax = round(sales_tax, 2)
tip_split = round(tip, 2) / 2
split_total = food_w_tax + tip_split

print("Your Tip comes out to $", tip_new)

split_tip_input = int(float(
    input("Would you like to split the tip with someone else? 0 = Yes  1= No ")))
if split_tip_input == 0:
    print("You both pay the following as a Tip $", tip_split)
    print("Your total is $", split_total)
elif split_tip_input == 1:
    print("Your total is $", new_total)

print("Sales Tax:", new_sales_tax)


# Tax Calculator
