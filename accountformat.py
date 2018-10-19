'''
Created on Oct 17, 2018

@author: jmullen19
'''
name1=input("Please enter the first account holder's name:")
accnum1=input('Please enter the first account number:')
acctype1=input('Please enter the type of account:')
balance1=float(input('Please enter the balance:'))
name2=input("Please enter the second account holder's name:")
accnum2=input('Please enter the second account number:')
acctype2=input('Please enter the type of account:')
balance2=float(input('Please enter the balance:'))
name3=input("Please enter the third account holder's name:")
accnum3=input('Please enter the third account number:')
acctype3=input('Please enter the type of account:')
balance3=float(input('Please enter the balance:'))

print('All Accounts:')
print('Acc Num:', format(accnum1,'>011s'), 'Name:', format(name1,'>11s'), 'Account:', format(acctype1,'>10s'), 'Bal:',format(balance1,'>.2f'))
print('Acc Num:', format(accnum2,'>011s'), 'Name:', format(name2,'>11s'), 'Account:', format(acctype2,'>10s'), 'Bal:',format(balance2,'>.2f'))
print('Acc Num:', format(accnum3,'>011s'), 'Name:', format(name3,'>11s'), 'Account:', format(acctype3,'>10s'), 'Bal:',format(balance3,'>.2f'))