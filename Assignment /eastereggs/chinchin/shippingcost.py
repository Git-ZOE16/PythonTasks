#Pseudocode
    #Step1. Enter the weight.
    #Step2. Determine price based on weight ranges.
    #Step3. If > 20, display error.
    #Step4. print the shipping cost

#Code

weight = float(input("Enter weight: "))
if 0 < weight <= 2: cost = 2.5
elif 2 < weight <= 4: cost = 4.5
elif 4 < weight <= 10: cost = 7.5
elif 10 < weight <= 20: cost = 10.5
else: cost = "Cannot be shipped"
print("Shipping cost:", cost)

