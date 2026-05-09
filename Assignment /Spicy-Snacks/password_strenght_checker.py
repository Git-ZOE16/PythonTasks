#Pseudocode:
    #Step1. Collect password string from the user.
    #Step2. Use len() to find the number of characters in the password.
    #Step3. Check the length against the rules: Less than 1: Invalid,  Less than 6: Weak, Between 7 and 10: Medium, Greater than 10: Strong



password = input("Enter your password: ")


length = len(password)


if length < 1:
    print("Strength: Invalid")
elif length < 6:
    print("Strength: Weak")
elif length <= 10:
    print("Strength: Medium")
else:
    print("Strength: Strong")



 
 
