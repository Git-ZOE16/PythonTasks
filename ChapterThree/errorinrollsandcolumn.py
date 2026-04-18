#What the code does is that

#It prints a grid (10x10) of < and > symbols in each roll and column.
#row % 2 == 1 checks if the row number is odd.
#If the row is odd, it prints <. If even, it prints >.
#The result is alternating rows of 10 symbols each.

#CODE 

for row in range(10):
    for column in range(10):
        print('<' if row % 2 == 1 else '>', end='')
    print()
        
    
