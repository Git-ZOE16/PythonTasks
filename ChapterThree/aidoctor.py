#The result shows that the entity at the other end is does not exhibit intelligent behavior
#because it doesn't listen to the problem, rather it only follows a complex script. 


response1 = yes
response2 = no
ai_doctor = input('What is your problem? ')
while True:
    ai_doctor = input('Have you had this problem before (yes or no)? ')
    if response1 == 'yes':
        print('Well, you have it again.')
        break
    elif response2 == 'no':
        print('Well, you have it now.')
        break



