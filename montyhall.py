'''
Created on Nov 16, 2018

@author: Jennie Mullen
Monty Hall problem
'''

from random import randint
car=randint(1,3)
guess=int(input('Which door would you like to pick:'))
print('The car was behind Door #', car)
print('You picked Door#', guess)

