month = int(input("Month (1-12): "))
names = ["", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
if 1 <= month <= 12: print(names[month])
else: print("Error")
