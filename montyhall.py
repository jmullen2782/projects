'''
Created on Nov 16, 2018

@author: Jennie Mullen
Monty Hall problem
'''

from random import randint
car=randint(1,3)
guess=int(input('Which door would you like to pick:'))
goat= not car
if car==1==guess:
    print('There is a goat behind Door #2')
    guess2=input('Would you like to change your pick?')
    if guess2.lower()='yes':
        print('You won!')
    else:
        print('You lost :(')
elif car==1 and guess==2:
    print('There is a goat behind Door #3')
    guess2=input('Would you like to change your pick?')
    if guess2.lower()='yes':
        print('You won!')
    else:
        print('You lost :(')
elif car==1 and guess==3:
    print('There is a goat behind Door #2')
    guess2=input('Would you like to change your pick?')
    if guess2.lower()='yes':
        print('You won!')
    else:
        print('You lost :(')
        
if car==2 and guess==1:
    print('There is a goat behind Door #3')
    guess2=input('Would you like to change your pick?')
    if guess2.lower()='yes':
        print('You won!')
    else:
        print('You lost :(')
elif car==2==guess:
    print('There is a goat behind Door #2')
    guess2=input('Would you like to change your pick?')
    if guess2.lower()='yes':
        print('You won!')
    else:
        print('You lost :(')
elif 
print('The car was behind Door #', car)
