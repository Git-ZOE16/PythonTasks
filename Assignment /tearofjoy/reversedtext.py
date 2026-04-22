#Pseudocode

#Step1 Enter a text
#Step2 Set reversed text to empty
#Step3 Add character to the front of each reversed text
#Step5 print the reveresed text


#CODE

text = input("Enter a text: ")
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text
print(f" reversed: {reversed_text}")

