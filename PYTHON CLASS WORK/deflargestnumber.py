def largest(number1, number2, number3):
    largest = number1
    if number2 > largest:
        largest = number2
            
    elif number3 > largest:
        largest = number3
    return largest   
    
         
print (largest(50, 30, 10)) #position argument
print(largest(number3=50,number1=100,number2=20)) #keyword argument
 
