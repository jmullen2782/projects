'''
Created on Apr 4, 2019

@author: Jennie Mullen
'''
import string
alphabet = []
for c in string.ascii_lowercase:
    alphabet.append(c)
ralpha = []
for i in alphabet:
    ralpha.reverse(i)
def main():
    text = input("Please enter a file name: ")
    