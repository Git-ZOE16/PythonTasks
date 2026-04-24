amount = float(input("Enter investment amount: "))
annual_rate = float(input("Enter annual interest rate (e.g. 3 for 3%): "))
years = int(input("Enter number of years: "))

monthly_rate = (annual_rate / 100) / 12
future_value = amount * (1 + monthly_rate)**(years * 12)

print("Accumulated value is", future_value)


