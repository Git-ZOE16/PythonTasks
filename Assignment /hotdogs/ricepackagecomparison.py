weight1 = float(input("Enter weight of package 1: "))
price1 = float(input("Enter price of package 1: "))
weight2 = float(input("Enter weight of package 2: "))
price2 = float(input("Enter price of package 2: "))

price_per_unit1 = price1 / weight1
price_per_unit2 = price2 / weight2

if price_per_unit1 < price_per_unit2:
    print("Package 1 has a better price.")
elif price_per_unit2 < price_per_unit1:
    print("Package 2 has a better price.")
else:
    print("Both have the same price.")

