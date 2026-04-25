#Pseudocode
    #Step1. Enter a number.
    #Step2. (a) number % 4 == 0 and number % 5 == 0.
    #Step3. (b) number % 4 == 0 or number % 5 == 0.
    #Step4. (c) Use ^ (exclusive or) logic.

#Code
number = int(input("Enter integer: "))
print("Both 4 and 5:", number % 4 == 0 and number % 5 == 0)
print("4 or 5:", number % 4 == 0 or number % 5 == 0)
print("4 or 5 but not both:", (number % 4 == 0) != (number % 5 == 0))







