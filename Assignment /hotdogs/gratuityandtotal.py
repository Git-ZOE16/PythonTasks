#Pseudocode
    #Step1. Enter the subtotal rate
    #Step2. Enter the gratuity rate
    #Step3. Calculate gratuity by multiplying subtotal by (rate / 100).
    #Step4. Initailize total and add subtotal + gratuity
    #Step5. Print the both gratuity and total.

#Code

subtotal = float(input("Enter the subtotal: "))
gratuity_rate = float(input("Enter the gratuity rate: "))

gratuity = subtotal * (rate / 100)
total = subtotal + gratuity

print("The gratuity is $", gratuity, "and total is $", total)

