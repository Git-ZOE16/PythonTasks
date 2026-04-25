number = int(input("Enter a three digit integer: "))
if (number // 100) == (number % 10):
    print("Palindrome")
else:
    print("Not palindrome")

