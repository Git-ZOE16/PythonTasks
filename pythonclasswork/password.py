#Pseudocode

#Step1 Enter user password
#Step2 if password strength is less than 8
#Step3 print password strength is very weak
#Step4 elif password strength is equal 8
#step5 print password strength is weak
#step6 elif password strength is less than equal to 16
#step7 print password strength is strong
#step8 else
#step9 print password strenght is very strong

#CODE

password_strength = input("Enter your password: ")
password_strength = len(password_strength)
if password_strength < 8:
   print("very weak")
elif (password_strength) == 8:
   print("weak password")
elif password_strength <= 16:
   print("strong")
else:
   print("very strong")
