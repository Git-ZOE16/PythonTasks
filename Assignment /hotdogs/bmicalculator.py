weight_pounds = float(input("Enter weight in pounds: "))
height_inches = float(input("Enter height in inches: "))

kg = weight_pounds * 0.45359237
meters = height_inches * 0.0254

bmi = kg / (meters**2)
print("BMI is", bmi)
