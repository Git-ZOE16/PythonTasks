#Pseudocode
#Step1. Enter the minutes.
#Step2. Calculate total days (minutes / 60 / 24).
#Step3. Calculate years (days / 365).
#Step4. Calculate remaining days (days % 365).
#Step5. Print the minuts, years and days

#Python Code

minutes = int(input("Enter the number of minutes: "))

days = minutes // (60 * 24)
years = days // 365
remaining_days = days % 365

print(minutes, "minutes is approximately", years, "years and", remaining_days, "days")
