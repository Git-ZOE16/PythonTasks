#Pseudocode
    #Step1. Enter the side length and the height (length) of the prism.
    #Step2. Calculate the area of the triangular base.
    #Step3. Multiply the area by the length to get the volume.
    #Step4. Print the area
    #Step5. Print the volume

#Code
side = float(input("Enter side of triangle: "))
length = float(input("Enter length of prism: "))

area = (3**0.5 / 4) * (side**2)
volume = area * length

print("The area is", area)
print("The volume is", volume)


