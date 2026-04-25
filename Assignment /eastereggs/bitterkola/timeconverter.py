number_of_minute = int(input("Enter your time range "))
day = number_of_minute // 1440
remaining_minute = number_of_minute % 1440
hour = remaining_minute % 60
minute = remaining_minute % 60
print(f"{day} days: {hour} hours: {minute} minutes")
