'''
Created on Nov 28, 2018
@author: Jennie Mullen
Monty Hall Problem
'''
simulator=int(input('How many times would you like to run the simulations?'))
while simulator<10 or simulator>10000:
    simulator=int(input('Invalid number, enter number between 10 and 10,000 '))
switch=input('Should the player switch or stay?')
while switch!='stay' and switch!='switch':
    print('Must either enter "switch" or "stay"')
    switch=input('Please try again')

win=0
for simulator in range(0, simulator+1): 
    from random import randint
    car=randint(1,3)
    door=randint(1,3)
    if car==1==door:
        if switch=='stay':
            win+=1
    elif car==1 and door==2:
        if switch=='switch':
            win+=1
    elif car==1 and door==3:
        if switch=='switch':
            win+=1
    if car==2 and door==1:
        if switch=='switch':
            win+=1
    elif car==2==door:
        if switch=='stay':
            win+=1
    elif car==2 and door==3:
        if switch=='switch':
            win+=1
    if car==3 and door==1:
        if switch=='stay':
            win+=1
    elif car==3 and door==2:
        if switch=='switch':
            win+=1
    elif car==3==door:
        if switch=='stay':
            win+=1
            
percent=(win/simulator)*100
print('You won', win, '/', simulator, '(', percent, '%)')
