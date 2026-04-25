user_pin = int(input(" Enter your four digit PIN "))
if user_pin >= 1000 and user_pin <= 9999:
    print("PIN is valid")
else:
    print("Invalid PIN")
