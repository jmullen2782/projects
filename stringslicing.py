'''
Created on Oct 22, 2018

@author: jenniemullen
'''
string=input('Please enter a String:')
startSlice=int(input('Please enter the index where you would like to start slicing:'))
endSlice=int(input('Please enter the index where you would like to stop slicing:'))
character=int(input('Please enter the index of a character you would like to access:'))
ch=string[character]
print('Original String:', string)
print('Length of the String:', len(string))
print('Substring from index', startSlice, 'to index', endSlice, ':', string[startSlice:endSlice])
print('Character at index', character, ':', ch)