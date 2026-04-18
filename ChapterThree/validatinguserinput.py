#Step1 Declear pass to be 0
#Step2 Declear failure to be 0
#Step3 Enter users result
#while result is not 1 and is not 2
#Print invalid
#Enter users result
#if result is add 1 to pass
#else add 1 to failure
#Print total pass and failure


#CODE

passes = 0
failure = 0

result = int(input('Enter result: '))
while result != 1 and result != 2:
    print = ("Invalid input: ")
        
if result == 1:
    passes += 1
else:
    failures += 1

print(f'Passes: {passes}\nFailure: {failure}')






