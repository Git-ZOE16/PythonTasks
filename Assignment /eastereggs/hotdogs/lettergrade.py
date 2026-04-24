#Pseudocode
    #Step1. Enter the score.
    #Step2. Use if-elif to check which range the score falls into.
    #Step3. Print the letter grade.

#Code

score = float(input("Enter score (0-100): "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")


