import random
## This is guess the number game 
print('Hello !!! What is your name ???')
name = input()
secnum = random.randint(1,20)
print('Well,'+ name + ' ....I am thinking of number between 1 - 20')

##This is allowing user to guess the number (max guess --> 6)
print('You have six guesses !!!')
for i in range (1,7):
    num = int(input('Enter the number !!!'))
    if num > secnum:
        print('It is too high')
    elif num <secnum:
        print('It is too low ')
    else:
        break
##Checking whether he won or lost 
if i<=6:
    print('WOOOOOOH !!!!You won ..!!!You took '+str(i)+' guesses')
else:
    print('You 1ost ')
    
