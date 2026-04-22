#Pseudocode

#Step1 Set number of attempt to 0
#Step2 while attempts is less than 3
#Step3 Request for password
#Step5 if password is correct
#Step6 print access granted 
#Step7 elif add 1 to number of attempt
#Step8 print "locked out"


#CODE

number_of_attempt = 0
while number_of_attempt < 3:
    password = input(" password: ")
    if password == "oluyemi0916":
        print("Access granted")
        break
    number_of_attempt += 1
if number_of_attempt == 3:
    print("Locked out")

