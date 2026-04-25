#Pseudocode
    #Step1. Enter month and year.
    #Step2. If month is 2, check if year is leap (divisible by 4 and not 100, or divisible by 400).
    #Step3. If leap, 29 days; elif 28.
    #Step4. For other months, assign 30 or 31.

#Code
month = int(input("Enter month (1-12): "))
year = int(input("Enter year: "))

if month == 2:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("29 days")
    else:
        print("28 days")
elif month in [4, 6, 9, 11]:
    print("30 days")
else:
    print("31 days")

