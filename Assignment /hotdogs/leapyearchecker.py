#Pseudocode
    #Step1. Enter the year.
    #Step2. Check if (year is divisible by 4 AND not 100) OR (divisible by 400).
    #Step3. Print if it is a leap year or not.

#Code
year = int(input("Enter a year: "))

is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if is_leap:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")


