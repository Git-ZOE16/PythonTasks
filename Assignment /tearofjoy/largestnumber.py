#Pseudocode

#Step1 Set largest to none
#Step2 Enter user input
#Step3 if input is done, break the loop
#Step5 if number is greather than largest
#Step6 let largest be the number
#Step7 print the largest


#CODE

largest = None
while True:
    user_input = input("Enter a number: ")
    if user_input == "done":
        break
    number = int(user_input)
    if largest is None or number > largest:
        largest = number
print(f"Largest: {largest}")

