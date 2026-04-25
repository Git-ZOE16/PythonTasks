#Pseudocode
    #Step1. Computer picks 0, 1, or 2.
    #Step2. User inputs 0, 1, or 2.
    #Step3. Check win/loss/draw conditions.

#Code
import random
computer = random.randint(0, 2)
user = int(input("Scissor(0), Rock(1), Paper(2): "))

if user == computer:
    print("It is a draw")
elif (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1):
    print("You won")
else:
    print("You lost")

