#Error in code: The code prints ('a =', a, '\nb =', b), the code is supposed to print variables a and b, but then,the variable is actually named nb in the string.
#Correction:a = b = 7 print('a =', a, 'b =', b)
#If you name a variable b, you must call it b. Putting \nb inside quotes will print a "new line" followed by the letter "b", not the value of the variable b.

#CODE
a = 7
b = 7
print(f'a = {a}\nb = {b}')
