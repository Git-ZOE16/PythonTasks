
#Pseudocode
    #Step1. Generate a random number between 1 and 7.
    #Step2. If 1, print Violet; if 2, Indigo; if 3, print Blue; if 4, print Yellow; if Orange, print Red;

#Code
import random
number = random.randint(1, 7)
colors = ["", "Violet", "Indigo", "Blue", "Green", "Yellow", "Orange", "Red"]
print("Color:", colors[number])

