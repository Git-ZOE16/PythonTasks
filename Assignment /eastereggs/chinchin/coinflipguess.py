#Pseudocode
    #Step1. Generate 0 or 1.
    #Step2. Prompt user for guess (0 or 1).
    #Step3. Compare and tell them if they are right.

#Code
import random
coin = random.randint(0, 1)
guess = int(input("Guess (0 for Head, 1 for Tail): "))
if guess == coin:
    print("Correct!")
else:
    print("Incorrect.")

