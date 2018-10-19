'''
Created on Oct 17, 2018

@author: jmullen19
'''
name1=input("Please enter the first account holder's name:")
accountnum1=input('Please enter the first account number:')
accounttype1=input('Please enter the type of account:')
balance1=float(input('Please enter the balance:'))
name2=input("Please enter the second account holder's name:")
accountnum2=input('Please enter the second account number:')
accounttype2=input('Please enter the type of account:')
balance2=float(input('Please enter the balance:'))
name3=input("Please enter the third account holder's name:")
accountnum3=input('Please enter the third account number:')
accounttype3=input('Please enter the type of account:')
balance3=float(input('Please enter the balance:'))

print('All Accounts:')
print('Acc Num:', format(accountnum1,'>011s'), 'Name:', format(name1,'>11s'), 'Account:', format(accounttype1,'>10s'), 'Bal:',format(balance1,'>.2f'))
print('Acc Num:', format(accountnum2,'>011s'), 'Name:', format(name2,'>11s'), 'Account:', format(accounttype2,'>10s'), 'Bal:',format(balance2,'>.2f'))
print('Acc Num:', format(accountnum3,'>011s'), 'Name:', format(name3,'>11s'), 'Account:', format(accounttype3,'>10s'), 'Bal:',format(balance3,'>.2f'))