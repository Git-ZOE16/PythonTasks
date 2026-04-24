#Pseudocode
    #Step1. Enter the  weight of water, initial temperature, and final temperature.
    #Step2. initialize energey to be  Q = M times (fina temperature - initial    temperature) times 4184.
    #Step3. Print the energy

#Python Code

m = float(input("Enter the amount of water in kilograms: "))
initial_temperature = float(input("Enter the initial temperature: "))
final_temperature = float(input("Enter the final temperature: "))

energy = m * (final_temp - initial_temp) * 4184
print("The energy needed is", energy)

