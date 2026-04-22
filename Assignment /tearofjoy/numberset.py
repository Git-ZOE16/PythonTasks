#Pseudocode

#Step1 Initialize total to 0
#Step2 Initialize count to 0
#Step3 Add item to total
#Step5 Add 1 to count
#Step6 print total divided by count


#CODE

numbers = [4,8,15,16,23,42,10,5,4,7,20]
total = 0
count = 0
for items in numbers:
    total += items
    count += 1
    print("f Average: {total / count}")
