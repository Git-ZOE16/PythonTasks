principal = int(input("Enter the principal amount: "))
annualrate = float(input("Enter the annual rate in: "))
duration = int(input("Enter the duration in years: ")) 
principal = annualrate*(1+annualrate)** duration/(1+annualrate)*duration-1
mortgage = principal
print("mortgage is:", mortgage)
