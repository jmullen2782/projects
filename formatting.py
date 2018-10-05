'''
Created on Oct 5, 2018

@author: jmullen19
'''
rate= float(input('Please enter your hourly rate:'))
hours=float(input('Please enter number of hours you work'))
weekpay= (rate*hours)*7
monthpay=weekpay*4
anualpay=monthpay*12
print('Weekly pay:', weekpay)
print('Monthly pay:', monthpay)
print('Anual pay:', anualpay)

