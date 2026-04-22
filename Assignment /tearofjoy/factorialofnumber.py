#Pseudocode

#Step1 Ask user for n
#Step2 Initialize result to 1
#Step3 while n is grather than 0
#Step4 multiply factorial by n
#Step5 Minus 1 from n
#Step6 print the result of factorial

#CODE
n = int(input("Enter n: "))
result = 1
while n > 0:
    result *= n
    n -= 1
print(f"Factorial: {result}")

