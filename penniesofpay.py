'''
Created on Jan 2, 2019
@author: Jennie Mullen
'''
days = int(input('Please enter number of days worked: '))
total = .01
print('Salary\tDays')
print('---------------')
for days in range(2,days+1,1):
    total*=2
    print('$', total,'\t',days, '\t')
print('You earned a total of $', total, 'in', days, 'days.')