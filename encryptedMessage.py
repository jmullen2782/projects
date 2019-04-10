'''
Created on Apr 4, 2019

@author: Jennie Mullen
'''
import string
alpha = []
for c in string.ascii_lowercase:
    alpha.append(c)
ralpha = []
for i in alpha:
    ralpha.reverse(i)
shift = 3
def main():
    text = input("Please enter a file name: ")
    text.open()
    text.readline()
    text.write()
    for letter in text:
        
        
    