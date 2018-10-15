'''
Created on Oct 15, 2018

@author: jmullen19
'''
name=input('Please enter your name:')
print('Hello,', name,',welcome to the Algebra and geometry calculator')
input('Press Enter to Continue')
print('\n')
print('Area of the Triangle:')
baseT=float(input('Please enter value of base of triangle:'))
heightT=float(input('Please enter value of height of triangle:'))
areaT=(baseT*heightT)/2
num=areaT
print('The area of the triangle is', format(num,'6.2f'), 'cm^2')
input('Press Enter to continue')
print('\n')
print('Volume of a Cube:')
sideC=float(input('Please enter value of side of cube:'))
volumeC=sideC**3
num=volumeC
print('The area of the triangle is', format(num,'8.2f'), 'cm^3')
print('\n')
print('Goodbye,', name, ',thank you for using this calculator')

