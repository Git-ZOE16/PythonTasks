scalene1 = float(input("Enter side 1: "))
scalene2 = float(input("Enter side 2: "))
scalene3 = float(input("Enter side 3: "))

#validity_checking

if (scalene1 + scalene2 > scalene3) and (scalene1 + scalene3 > scalene2) and (scalene2 + scalene3 > scalene1):
    if scalene1 == scalene2 == scalene3:
        print("Equilateral triangle")
    elif scalene1 == scalene2 or scalene2 == scalene3 or scalene1 == scalene3:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")
else:
    print("Not a valid triangle.")



