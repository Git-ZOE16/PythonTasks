#Pseudocode

#Step1 Initialize total to 0
#Step2 Enter a number
#Step3 while number is not 0
#Step4 add number to total
#Step5 Ask for a number again
#Step6 print the total

#CODE

total = 0
number = int(input("Enter a number: "))
while number != 0:
    number += total
    number = int(input("Enter a number: "))
print(F"total: {total}")
