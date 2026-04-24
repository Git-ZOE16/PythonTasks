#Pseudocode:*
#Step1. Input a, b, and c.
#Step2. Calculate the discriminant: D = b^2 - 4ac.
#Step3. If D > 0, calculate and show two roots.
#Step4. If D = 0, calculate and show one root.
#Step5. If D < 0, say there are no real roots.

#Code

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    root1 = (-b + discriminant**0.5) / (2*a)
    root2 = (-b - discriminant**0.5) / (2*a)
    print("The roots are", root1, "and", root2)
elif discriminant == 0:
    root = -b / (2*a)
    print("The root is", root)
else:
    print("The equation has no real roots.")


