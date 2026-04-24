#Pseudocode
    #Step11. Enter the total seconds.
    #Step2. Find hours (seconds // 3600).
    #Step3. Find remaining seconds after hours are taken.
    #Step4. Find minutes (remaining // 60).
    #Step5. Find final remaining seconds (remaining % 60).
    #Step6. Print seconds,hours,minutes and finalseconds

#Code
seconds = int(input("Enter seconds: "))

hours = seconds // 3600
remaining_seconds = seconds % 3600
minutes = remaining_seconds // 60
final_seconds = remaining_seconds % 60

print(seconds, "seconds =", hours, "hour,", minutes, "minutes, and", final_seconds, "seconds")

