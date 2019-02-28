'''
Created on Feb 28, 2019

@author: jmullen19
'''
from algebrageometrycalc import num
numbers = open('grades.txt','r')
total = 0
line = numbers.readline()

while line != '':
    num = int(line.rstrip())
    total += num
    line = numbers.redline()
numbers.close()
print(total)

