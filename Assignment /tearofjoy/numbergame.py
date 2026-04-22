#Pseudocode

#Step1 select a random number from 1 to 100
#Step2 set attempt to 0
#Step3 Dice until guess is matched
#Step5 Enter guess
#Step6 Add 1 to the attempts
#Step7 if the guess is high
#Step8 print lower
#Step9 if the guess is low
#Step10 print higher
#Step11 print success and attempts


#CODE
import random
secret = random.randint(1, 100)
guess = 0
attempts = 0
while guess != secret:
    guess = int(input("Guess: "))
    attempts +=1
    if guess > secret:
        print("Higher")
    elif guess < secret:
        print("Lower")
    elif secret == correct:
        print(f"correct! ({attempts} attempts)")
