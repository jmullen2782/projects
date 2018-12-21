'''
Created on Dec 17, 2018

@author: jmullen19
'''
import random
roll = random.randint(1,6)
target=int(input('Please enter a valid number from 1 to 6:'))
while target<0 or target>6:
    target=int(input('Please enter a valid number from 1 to 6:'))
    again = int("Press enter to roll again")
while 1>=target>=6:
    print('You rolled', roll)
    again = int('Please enter to roll again')
while target==roll:
        print('It took you', roll, 'tries to roll the target number.')
        
        
        