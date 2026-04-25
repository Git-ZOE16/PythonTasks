#Pseudocode
    #Step1. Enter 3-digit number.
    #Step2. Use floor division and modulo to extract digits.
    #Step3. Add all the digits
    #Step4. Print the Sum

#Code

number = int(input("Enter 3-digit number: "))
digit1 = number // 100
digit2 = (number // 10) % 10
digit3 = number % 10
print("Sum:", digit1 + digit2 + digit3)

