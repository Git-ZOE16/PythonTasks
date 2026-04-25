#Pseudocode
    #Step1. Input status and income.
    #Step2. Use nested if statements to find the correct tax bracket based on status.
    #Step3. print tax
   
   
#Code

status = int(input("Enter status (0-3): "))
income = float(input("Enter taxable income: "))

if status == 0:
    if income <= 8350: tax = income * 0.10
    elif income <= 33950: tax = 835 + (income - 8350) * 0.15
    
print(f"Tax: ${tax}")

