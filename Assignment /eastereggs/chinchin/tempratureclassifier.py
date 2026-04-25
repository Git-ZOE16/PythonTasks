temperature = float(input("Celsius: "))
if temperature < 0: print("Freezing")
elif 0 <= temperature <= 15: print("Cold")
elif 16 <= temperature <= 25: print("Warm")
else: print("Hot")

