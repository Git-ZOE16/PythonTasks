#Pseudocode
    #Step1. Enter number between 0 and 1000.
    #Step2. Initialize digit1 and use % 10 to get the last digit.
    #Step3. Use // 10 to remove the last digit from number.
    #Step4. Iterate and add them together.
    #Step5. Print the sum of the digits

#Code
number = int(input("Enter a number between 0 and 1000: "))

digit1 = number % 10
number = number // 10

digit2 = number % 10
number = number // 10

digit3 = number % 10

total_sum = digit1 + digit2 + digit3
print("The sum of the digits is", total_sum)

