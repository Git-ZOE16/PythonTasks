number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

# Simple swap logic
if number1 > number2:
    number1, number2 = number2, number1
if number2 > number3:
    number2, number3 = number3, number2
if number1 > number2:
    num1, number2 = number2, number1

print("Sorted numbers:", number1, number2, number3)

