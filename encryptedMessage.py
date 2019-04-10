'''
Created on Apr 4, 2019

@author: Jennie Mullen
'''
import string
alpha = []
for c in string.ascii_lowercase:
    alpha.append(c)
shift = 3
ealpha = []
for i in alpha:
    rshift = shift*-1
    
def main():
    text = input("Please enter a file name: ")
    text.open()
    text.readline()
    text.write()
    for letter in text:
        
        
    