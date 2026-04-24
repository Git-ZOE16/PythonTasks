#Pseudocode
#Step1. Enter a three-digit number.
#Step2. Find the first digit (divide by 100).
#Step3. Find the last digit (use remainder %).
#Step4. If the first and last digits are the same, it's a palindrome.

#Code
number = int(input("Enter a three-digit integer: "))
number = abs(number) # Treat negative as positive

first_digit = number // 100
last_digit = number % 10

if first_digit == last_digit:
    print(number, "is a palindrome")
else:
    print(number, "is not a palindrome")


