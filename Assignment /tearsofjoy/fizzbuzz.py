#Pseudocode

#Step1 for numbers in range 1 to 51
#Step2 If number is divisible by 3, print "FizzBuzz"
#Step3 elif number is divisible by 3 print Fizz
#Step4 elif divisible by 5, print "Buzz"
#Step5 elif print the number


#CODE

for number in range(1, 51):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz", end=" ")
    elif number % 3 == 0:
        print("Fizz", end=" ")
    elif number % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(number)
