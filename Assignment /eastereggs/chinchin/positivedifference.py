#Pseudocode:*
    #Step1. Generate two random single-digit numbers.
    #Step2. Subtract the smaller from the larger (or use absolute value).

#Code
import random
a = random.randint(0, 9)
b = random.randint(0, 9)
diff = abs(a - b)
print(f"Difference between {a} and {b} is {difference}")

