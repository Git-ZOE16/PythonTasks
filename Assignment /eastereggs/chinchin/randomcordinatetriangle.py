#Pseudocode
    #Step1. Width is 50, so x is between -25 and 25.
    #Step2. Height is 150, so y is between -75 and 75.
    #Step3. Generate random x and y.
 
#Code
import random
x = random.uniform(-25, 25)
y = random.uniform(-75, 75)
print(f"Random point: ({x}, {y})")
