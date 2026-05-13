
#Exercise4.13 Arbitrary Argument List

def product(args):
    result = 1
    for value in args:
        result *= value
    return result

print(product(1, 2, 3))    
print(product(5, 10, 2))  
